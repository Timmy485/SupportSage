"""App factory file"""
from flask import Flask, request, abort
import os
from app.config.config import CONFIGS
from flask_sqlalchemy import SQLAlchemy
import logging
from flask_limiter import Limiter, HEADERS
from flask_limiter.util import get_remote_address
from flask_cors import CORS

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

database = SQLAlchemy()

limiter = Limiter(get_remote_address,
                  header_name_mapping={
                      HEADERS.LIMIT: "X-My-Limit",
                      HEADERS.RESET: "X-My-Reset",
                      HEADERS.REMAINING: "X-My-Remaining"
                    },
                  default_limits=["200 per day", "50 per hour"],
                  storage_uri="memory://"
                )


def create_app():
    """App factory"""
    application = Flask(__name__)
    CORS(application)
    # db.init_app(app)0
    config_name = os.getenv('FLASK_ENV', 'default')

    # Using a environment configuration
    application.config.from_object(CONFIGS[config_name])
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Import declared routes
    from app.api.routes import route_blueprint

    # Request rate limiter
    limiter.init_app(application)

    database.init_app(application)
    # Register blueprint apps
    application.register_blueprint(route_blueprint, url_prefix="/api")
    return application
