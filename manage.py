#!/usr/bin/env python2
# -*- encoding:utf-8 -*-
import os
from flask import Flask
from flask.ext.script import Manager
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == "__main__":
    manager.run()

