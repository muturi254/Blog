class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ashorta:Number12@localhost/blog'
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = '123'

config_options ={"production":ProdConfig,"default":DevConfig}

