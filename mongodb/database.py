from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from mongodb.models import User
from config import settings

MONGODB_MODELS=[User]

async def mongo_init():
    client = AsyncIOMotorClient(settings.get_mongo_uri())
    project = "main"
    await init_beanie(database=client[project], document_models=MONGODB_MODELS)