import os 

from langchain_openai import ChatOpenAI


def create_llm() -> ChatOpenAI:
    """Create the shared LLM instance used by agents"""
    
    return ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0,
    )