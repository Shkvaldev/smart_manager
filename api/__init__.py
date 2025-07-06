from quart import Quart, request, redirect, url_for, render_template, session, g
from quart_cors import cors
from loguru import logger
from config import settings

from api.routers.new_message import router as new_message_router
from api.routers.healthcheck import router as healthcheck_router
from api.routers.new_faq import router as new_faq_router

from ai import ai_provider

app = Quart(__name__)
app.secret_key = 'supersecret'

app = cors(app, allow_origin="*")

app.register_blueprint(healthcheck_router)
app.register_blueprint(new_message_router) 
app.register_blueprint(new_faq_router) 

def create_app():
    return app