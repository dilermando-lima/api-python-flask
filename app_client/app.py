from flask import Flask
from app_client.settings import settings_local
from app_client.app_client.client_resources import client_resources
from app_client.app_client.models import db
from app_client.app_client.handle_excep import error_handle

def create_app():
    app = Flask(__name__)
    app.config.from_object(settings_local)
    app.register_blueprint(client_resources)
    app.register_blueprint(error_handle)
    db.init_app(app)
    return app

