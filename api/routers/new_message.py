from quart import Blueprint, request
from loguru import logger

from mongodb.database import mongo_init
from mongodb.services import MongoBaseService

router = Blueprint(
    name='message_new_router',
    import_name='message_new_router'
)

# Handling new messages in JSON format
@router.post("/message/new")
async def post_route():
    try:
        await mongo_init()
        return {"status": "ok"}, 200
    except Exception as e:
        logger.error(f"Failed to handle new message: {e}")
        return {"error": "Failed to handle new message: {e}"}, 500