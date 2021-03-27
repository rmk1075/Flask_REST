from flask import Flask

from pREST import __init__
from pREST.rest import room
from pREST.settings import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(room.blueprint)

    return app
