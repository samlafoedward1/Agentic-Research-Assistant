import os 

from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()


def create_llm() -> ChatOllama:
    """Create the shared LLM instance used by agents"""
    
    model_name = os.getenv(
        "LLM_Model",
        "qwen2.5:7b",
    )
    
    return ChatOllama(
        model=model_name,
        temperature=0,
    )