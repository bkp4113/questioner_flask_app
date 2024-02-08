# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
import logging
import sys

from flask import Flask
from app.question import question_ns
from flask import Blueprint
from flask_restx import Api

__name__ = 'questioner_app'


def create_app():

    app = Flask(__name__)
    api_v1 = Blueprint("api", __name__, url_prefix="/api/v1")

    api = Api(
        api_v1,
        version="1.0",
        title="Question API",
        description="A simple Question API",
        doc='/doc'
    )
    configure_logger(app)

    api.add_namespace(question_ns)
    app.register_blueprint(api_v1)
    app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
    app.config.SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'  # SQLite in-memory database
    return app


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
