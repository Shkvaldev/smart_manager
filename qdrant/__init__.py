import uuid
from typing import List
from qdrant_client import AsyncQdrantClient, models
from loguru import logger

from config import settings

class Qdrant:
    def __init__(self):
        self.client = AsyncQdrantClient(url=settings.qdrant_uri)

    async def connect(self) -> None:
        """Checking Qdrant connection"""
        try:
            # Creation of faq collection (collection of general company info)
            if not await client.collection_exists("faq"):
                await self.client.create_collection(
                    collection_name="faq",
                    vectors_config=models.VectorParams(size=settings.embeddings_size, distance=models.Distance.COSINE),
                )
            logger.success("Connection to Qdrant is established")
        except Exception as e:
            logger.error(f"Failed to connect to Qdrant: {e}")
            raise ValueError(e)
        
    async def add(self, embedding: List[float], payload: str) -> None:
        """Adding new info to Qdrant"""
        try:
            await client.upsert(
                collection_name="faq",
                wait=True,
                points=[
                    PointStruct(id=str(uuid.uuid4()), vector=embedding, payload={"text": payload}),
                ]
            )
            logger.success("New embedding is added to Qdrant")
        except Exception as e:
            logger.error(f"Failed to add new embedding to Qdrant: {e}")
            raise ValueError(e)

    async def search(self, query: List[float]) -> str | None:
        """Looking for a context from Qdrant"""
        if len(query) != settings.embeddings_size:
            logger.error(f"Failed to search in Qdrant: provided search embedding's length is wrong (need: {settings.embeddings_size}, in fact: {len(query)})")
            raise ValueError(f"Failed to search in Qdrant: provided search embedding's length is wrong (need: {settings.embeddings_size}, in fact: {len(query)})")
        try:
            search_result = client.search(
                collection_name="faq",
                query_vector=query,
                limit=1
            )
            print(search_result)
        except Exception as e:
            logger.error(f"Failed to add new embedding to Qdrant: {e}")
            raise ValueError(e)