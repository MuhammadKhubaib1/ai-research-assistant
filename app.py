import os
import shutil
import streamlit as st
from dotenv import load_dotenv

from src.ingest import load_and_split_pdf
from src.retriever import create_vectorstore, load_vectorstore
from src.qa_chain import get_llm, build_prompt

load_dotenv()

PERSIST_DIRECTORY = "chroma_db"

st.set_page_config(page_title="AI Research Assistant", page_icon="📘")
st.title("📘 AI Research Assistant")
st.write("Upload PDF documents and ask questions about their content.")

if "processed_files" not in st.session_state:
    st.session_state.processed_files = []

if "messages" not in st.session_state:
    st.session_state.messages = []

@st.cache_resource
def get_cached_llm():
    return get_llm()

@st.cache_resource
def get_cached_vectorstore():
    return load_vectorstore(persist_directory=PERSIST_DIRECTORY)

def reset_database():
    if os.path.exists(PERSIST_DIRECTORY):
        shutil.rmtree(PERSIST_DIRECTORY)
    st.cache_resource.clear()
    st.session_state.processed_files = []
    st.session_state.messages = []

with st.sidebar:
    st.header("Controls")
    if st.button("Reset documents"):
        reset_database()
        st.success("Documents and chat history cleared.")

uploaded_files = st.file_uploader(
    "Upload one or more PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    new_files = [f for f in uploaded_files if f.name not in st.session_state.processed_files]

    if new_files:
        save_dir = os.path.join("data", "uploads")
        os.makedirs(save_dir, exist_ok=True)

        all_chunks = []

        with st.spinner("Processing documents..."):
            for uploaded_file in new_files:
                file_path = os.path.join(save_dir, uploaded_file.name)

                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                chunks = load_and_split_pdf(file_path)
                all_chunks.extend(chunks)
                st.session_state.processed_files.append(uploaded_file.name)

            if all_chunks:
                create_vectorstore(all_chunks, persist_directory=PERSIST_DIRECTORY)
                st.cache_resource.clear()

        st.success(f"Processed {len(new_files)} new file(s).")

if st.session_state.processed_files:
    st.subheader("Loaded documents")
    for name in st.session_state.processed_files:
        st.write(f"- {name}")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("sources"):
            with st.expander("Sources"):
                for i, src in enumerate(message["sources"], start=1):
                    st.markdown(f"**Source {i}** — {src['page']}")
                    st.caption(src["source"])
                    st.write(src["text"])

question = st.chat_input("Ask a question about your uploaded PDFs")

if question:
    if not st.session_state.processed_files:
        st.warning("Please upload at least one PDF first.")
    else:
        st.session_state.messages.append({"role": "user", "content": question})

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Searching documents and generating answer..."):
                vectorstore = get_cached_vectorstore()
                retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
                docs = retriever.invoke(question)

                context = "\n\n".join([doc.page_content for doc in docs])

                prompt = build_prompt()
                llm = get_cached_llm()

                formatted_prompt = prompt.format_messages(
                    context=context,
                    question=question
                )
                response = llm.invoke(formatted_prompt)

                answer = response.content
                st.markdown(answer)

                sources = []
                with st.expander("Sources"):
                    for i, doc in enumerate(docs, start=1):
                        page = doc.metadata.get("page", "Unknown")
                        source = doc.metadata.get("source", "Unknown")
                        page_display = f"Page {page + 1}" if isinstance(page, int) else f"Page {page}"

                        st.markdown(f"**Source {i}** — {page_display}")
                        st.caption(source)
                        preview = doc.page_content[:500] + "..."
                        st.write(preview)

                        sources.append({
                            "page": page_display,
                            "source": source,
                            "text": preview
                        })

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer,
            "sources": sources
        })