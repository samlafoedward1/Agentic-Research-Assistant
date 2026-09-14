from langchain_community.tools import DuckDuckGoSearchResults

from schemas import RetrievedDocument


search_tool = DuckDuckGoSearchResults(
    output_format="list",
    max_results=5
)


def search_web(query: str) -> list[RetrievedDocument]:
    """Search the web and normalize the returned results"""
    
    results = search_tool.invoke(query)
    
    documents = []
    
    for result in results: 
        document = RetrievedDocument(
            title=result.get("title", ""),
            url=result.get("link", ""),
            content=result.get("snippet", ""),
        )
        
        documents.append(document)
    
    return documents


def retrieve_documents(
    search_queries: list[str],
) -> list[RetrievedDocument]:
    """Retrieve documents for all planner-generated search queries"""
    
    documents = []
    
    for query in search_queries:
        query_results = search_web(query)
        documents.extend(query_results)
        
    return documents
        