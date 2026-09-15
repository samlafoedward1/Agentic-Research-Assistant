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
        
    print("\nRetrieving information...\n")
    
    chunks = retrieve_documents(
        user_query=query,
        search_queries=plan.search_queries,
    )
    
    print(
        f"Selected {len(chunks)}"
        "relevant chunks.\n"
    )
    
    for index, chunk in enumerate(
        chunks,
        start=1,
    ):
        print(f"{index}. {chunk.title}")
        print(f"     {chunk.url}") 
        print(f"Similarity {chunk.score:.4f}")
        print(f".    {chunk.content[:250]}") 
        print()  
    
    
        
        
if __name__ == "__main__":
    main()