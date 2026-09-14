from typing import TypedDict

from schemas import RetrievedDocument

class ResearchState(TypedDict, total=False):
    """Shared state passed between nodes in research graph"""
    
    
    query: str
    
    query_type: str
    output_format: str
    search_queries: list[str]
    
    retrieved_documents: list[RetrievedDocument]
    
    retrieval_sufficient: bool
    retry_count: int
    
    final_answer: str