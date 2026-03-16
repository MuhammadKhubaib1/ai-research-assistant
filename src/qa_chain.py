from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


def get_llm():
    return ChatOllama(
        model="llama3.2:3b",
        temperature=0
    )


def build_prompt():
    template = """
You are an AI research assistant.

Answer the user's question only from the provided context.
If the answer is not in the context, say: "I could not find that in the uploaded document."

Rules:
- Keep the answer concise and clear.
- Use 3 to 5 sentences unless the user asks for more detail.
- Do not make up facts.
- Base the answer only on the provided context.

Context:
{context}

Question:
{question}
"""
    return ChatPromptTemplate.from_template(template)