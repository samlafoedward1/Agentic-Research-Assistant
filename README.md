# Agentic Research Assistant

A multi-agent research assistant built with LangGraph. A supervisor agent coordinates specialized sub-agents — planning, web retrieval, and summarization — with persistent memory across turns, structured output parsing with fallback logic, and reproducible evaluation via MLflow.

## Architecture

**Pattern:** Supervisor multi-agent graph, hand-built with tool-calling (not the `langgraph-supervisor` helper library).

```
Start → Supervisor → Planner → Supervisor → Retriever → Supervisor (check) → Summarizer → End
                                                  ↑___________________________|
                                                  (insufficient results, retry ≤2)
```

- **Planner** — classifies the query (general vs. technical) and decides the output format
- **Retriever** — searches the web (Tavily), embeds results into a vector store, retrieves relevant chunks
- **Summarizer** — produces the final answer in the format the planner chose
- **Supervisor** — routes between agents and checks retrieval sufficiency before handing off, with a bounded retry/fallback loop

## Key features

- **Dynamic output format** — short sourced answer or structured multi-paragraph report, decided per query
- **Structured output with fallback** — Pydantic schema enforced via `with_structured_output`, falling back to explicit tool-calling if native structured output fails
- **Persistent memory** — session-scoped conversation memory via LangGraph checkpointer (cross-session memory planned as v2)
- **Retrieval-augmented answers** — local Hugging Face `sentence-transformers` embeddings over Tavily search results
- **Reproducible evaluation** — MLflow tracking for both answer quality (vs. a Hugging Face benchmark dataset) and performance (latency, tokens, cost)

## Tech stack

LangGraph · OpenAI API · Tavily · Hugging Face (`sentence-transformers`, eval datasets) · Vector store (Chroma/FAISS) · MLflow · Streamlit · Python

## Status

🚧 In design — requirements and graph architecture finalized, implementation not yet started.
