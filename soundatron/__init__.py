# -*- encoding:utf-8 -*-
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from soundatron.views.frontend import frontend
from soundatron.views.configure import configure


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.register_blueprint(frontend, url_prefix='')
app.register_blueprint(configure, url_prefix='/configure')

