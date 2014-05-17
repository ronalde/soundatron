# -*- encoding:utf-8 -*-
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    MPDCONFIGURE = BASEDIR + "/scripts/mpd-configure"
    MPDPATH = "/var/lib/mpd"


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 't0p s3cr3t'


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'secret'


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
