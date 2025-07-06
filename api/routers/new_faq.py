from quart import Blueprint, request
from loguru import logger

from ai import ai_provider
from qdrant import Qdrant

router = Blueprint(
    name='faq_new_router',
    import_name='faq_new_router'
)

# Handling new entries for Qdrant
# Input: {"text": "Some new text info for Qdrant"}
@router.post("/faq/new")
async def post_route():
    try:        
        data = await request.json

        # Creating connection to Qdrant
        vdb = Qdrant()
        await vdb.connect()

        # Creating embedding
        embedding = ai_provider.embed(data["text"])
        if not embedding:
            return {"error": "Failed to generate embedding for text"}, 500
        
        # Pushing to Qdrant
        await vdb.add(embedding=embedding, payload=data["text"])

        return {"status": "ok"}, 200
    except Exception as e:
        logger.error(f"Failed to add new FAQ to Qdrant: {e}")
        return {"error": f"Failed to add new FAQ to Qdrant: {e}"}, 500