import os
from flask import Flask

from .models import db
from . import config


def create_app():
    app = Flask(__name__)
    db_user = os.environ.get('POSTGRES_DB_USER')
    db_psw = os.environ.get('POSTGRES_DB_PSW')
    db_host = os.environ.get('SERVICE_POSTGRES_SERVICE_HOST')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_psw}@{db_host}/test_envs'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    return app
