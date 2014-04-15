import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "1233466"
    APPLICATION_ROOT = basedir
    MPDCONFIGURE = APPLICATION_ROOT + "/scripts/mpd-configure"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,

    'production': ProductionConfig,
    'default': DevelopmentConfig
}
