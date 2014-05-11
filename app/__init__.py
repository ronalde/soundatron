# -*- encoding:utf-8 -*-
from flask import Flask
from config import config
from flask.ext.bootstrap import Bootstrap


bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)

    from .configure import configure as configure_blueprint
    app.register_blueprint(configure_blueprint)
    return app
