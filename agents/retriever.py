import faiss
import numpy as np

from langchain_community.tools import DuckDuckGoSearchResults

from chunking import chunk_text
from embeddings import FastEmbedder
from schemas import RetrievedChunk, RetrievedDocument
from web_loader import fetch_page_content


search_tool = DuckDuckGoSearchResults(
    output_format="list",
    max_results=5
)

embedder = FastEmbedder()


def search_web(query: str) -> list[RetrievedDocument]:
    """Search the web and normalize the returned results"""
    
    results = search_tool.invoke(query)
    
    documents = []
    
    for result in results: 
        documents.append(
            RetrievedDocument(
                title=result.get("title", ""),
                url=result.get("link", ""),
                content=result.get("snippet", ""),
            )
        )
    
    return documents


def deduplicate_documents(
    documents: list[RetrievedDocument],
) -> list[RetrievedDocument]:
    """Remove duplicate results using their URL"""
    
    unique_documents = {}
    
    for document in documents:
        if(
            document.url
            and document.url not in unique_documents
        ):
            unique_documents[document.url] = document
            
    return list(unique_documents.values())


def create_chunks(
    documents: list[RetrievedDocument],
) -> list[RetrievedChunk]:
    """Fetch webpages and split their contents into chunks"""
    
    chunks = []
    
    for document in documents:
        content = fetch_page_content(
            document.url
        )
        
        if not content:
            continue
        
        page_chunks = chunk_text(content)
        
        for page_chunk in page_chunks:
            chunks.append(
                RetrievedChunk(
                    content=page_chunk,
                    title=document.title,
                    url=document.url,
                )
            )
    return chunks
    
    
def rank_chunks(
    query: str,
    chunks: list[RetrievedChunk],
    top_k: int = 10,
 ) -> list[RetrievedChunk]:
    """Rank webpage chunks using FAISS semantic search"""   
     
    if not chunks:
        return []
     
    texts = [
        chunk.content
        for chunk in chunks
    ]
     
    document_vectors = np.array(
        embedder.embed_documents(texts),
        dtype="float32",
     )
     
    query_vector = np.array(
        embedder.embed_documents(texts),
        dtype="float32",
    )
     
    # Normalize vectors so inner product acts as cosine similarity
    faiss.normalize_L2(document_vectors)
    faiss.normalize_L2(query_vector)
     
    dimension = document_vectors.shape[1]
     
    index = faiss.IndexFlatIP(
        dimension
    )
     
    index.add(document_vectors)
     
    scores, indices = index.search(
        query_vector,
        min(top_k, len(chunks)),
    )
    
    ranked_chunks = []
     
    for score, index_position in zip(
        scores[0],
        indices[0],
    ):
        chunk = chunks[index_position]
         
        ranked_chunks.append(
            RetrievedChunk(
                content=chunk.content,
                title=chunk.title,
                url=chunk.url,
                score=float(score),
            )
         )
    return ranked_chunks
         
        
def retrieve_documents(
    user_query: str,
    search_queries: list[str],
) -> list[RetrievedChunk]:
    """Run the complete web retrieval pipeline"""
    
    documents = []
    
    for query in search_queries:
        query_results = search_web(query)
        documents.extend(query_results)
        
    documents = deduplicate_documents(
        documents
    )
    
    chunks = create_chunks(
        documents
    )
    
    ranked_chunks = rank_chunks(
        query=user_query,
        chunks=chunks,
    )
    
    return documents
        