class Config:
    SECRET_KEY = "1233466"

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
