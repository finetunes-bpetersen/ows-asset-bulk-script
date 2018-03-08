"""
Application.
The API application is a `flask` application. It provides simple features such
as registering a url for a specific handlers.
"""

from flask import Flask
from . import config
from sqlalchemy import create_engine

app = Flask(config.SERVICE_NAME)

db = create_engine(config.DB_URL)

#flask_request.setup(app, config.ENVIRONMENT)