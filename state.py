from typing import TypedDict


class ResearchState(TypedDict, total=False):
    """Shared state passed between nodes in research graph"""
    
    
    query: str
    
    query_type: str
    search_queries: list[str]
    
    retrieved_documents: list[dict]
    
    retrieval_sufficient: bool
    retry_count: int
    
    final_answer: str