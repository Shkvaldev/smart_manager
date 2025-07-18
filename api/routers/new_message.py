from quart import Blueprint, request
from loguru import logger

from mongodb.database import mongo_init
from mongodb.models import User
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
        
        data = await request.json
        # Searching for user
        try:
            user = await MongoBaseService.find(User, {"member_id": data["member_id"]})
        except Exception:
            # Create new user if not found
            user = await MongoBaseService.create(
                User,
                member_id=data["member_id"],
                name=data["name"]
            )
        
        # Deal with message

        return {"status": "ok", "user": user.name}, 200
    except Exception as e:
        logger.error(f"Failed to handle new message: {e}")
        return {"error": f"Failed to handle new message: {e}"}, 500