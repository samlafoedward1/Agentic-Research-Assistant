from typing import Literal

from pydantic import BaseModel, Field


class ResearchPlan(BaseModel):
    """Structured output produced by the planner agent."""
    
    
    query_type: Literal["general", "technical"]
    
    output_format: Literal[
        "short_answer",
        "detailed_report",
    ]
    
    search_queries: list[str] = Field(
        min_length=1,
        max_length=5,
    )
    

class RetrievedDocument(BaseModel):
    """Normalized document returned by the retriever"""
    
    title: str
    url: str
    content: str
    score: float | None = None
    