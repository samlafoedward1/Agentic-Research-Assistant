from agents.planner import create_research_plan
from agents.retriever import retrieve_documents

def main() -> None:
    query = input("Enter a research question: ")
    
    print("\nCreating research plan...\n")
    
    plan = create_research_plan(query)
    
    print(f"Query type: {plan.query_type}")
    
    print(f"Output format: {plan.output_format}")
    
    print("\n Search queries")
    
    for index, search_query in enumerate(
        plan.search_queries,
        start=1,
    ):
        print(f"{index}. {search_query}")
        
    print("\nRetrieving documents...\n")
    
    documents = retrieve_documents(
        plan.search_queries
    )
    
    print(f"Retrieved {len(documents)} documents.\n")
    
    for index, document in enumerate(
        documents[:10],
        start=1,
    ):
        print(f"{index}. {document.title}")
        print(f"     {document.url}") 
        print(f".    {document.content[:200]}") 
        print()  
    
    
        
        
if __name__ == "__main__":
    main()