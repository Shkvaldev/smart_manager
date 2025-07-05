from typing import List

from gigachat import GigaChat
from loguru import logger

from config import settings

class AI:
    def __init__(self, key: str) -> None:
        """GIGAChat provider constructor"""
        self.client = GigaChat(
            credentials=key
        )
        try:
            # Checking connection
            self.client.get_models()
            logger.success("GIGAChat instance is ready")
        except Exception as e:
            logger.error(f"Failed to init GIGAChat: {e}")

    def ask(self, query: str) -> str | None:
        """Asking GIGAChat"""
        try:
            response = self.client.chat(query)
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Failed to get answer from GIGAChat: {e}")

    def embed(self, payload: str) -> List[float] | None:
        """Making embeddings using GIGAChat"""
        try:
            response = self.client.embeddings([payload])
            return response.data[0].embedding
        except Exception as e:
            logger.error(f"Failed to get answer from GIGAChat: {e}")

ai_provider = AI(settings.gigachat_key)
