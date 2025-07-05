from quart import Blueprint
from loguru import logger

from mongodb.database import mongo_init

router = Blueprint(
    name='healthcheck_router',
    import_name='healthcheck_router'
)

@router.get("/health")
async def get_route():
    return {"status": "ok"}, 200