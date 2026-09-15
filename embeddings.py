import os

from dotenv import load_dotenv
from fastembed import TextEmbedding


load_dotenv()


DEFAULT_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


class FastEmbedder:
    """Generate local embeddings using FastEmbed."""

    def __init__(
        self,
        model_name: str | None = None,
    ) -> None:
        self.model_name = (
            model_name
            or os.getenv("EMBEDDING_MODEL")
            or DEFAULT_EMBEDDING_MODEL
        )
        
        print(f"Embedding model: {self.model_name}")

        self.model = TextEmbedding(
            model_name=self.model_name,
        )

    def embed_documents(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        embeddings = self.model.embed(texts)

        return [
            embedding.tolist()
            for embedding in embeddings
        ]

    def embed_query(
        self,
        text: str,
    ) -> list[float]:
        embedding = next(
            self.model.query_embed(text)
        )

        return embedding.tolist()