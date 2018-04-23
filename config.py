class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ashorta:Number12@localhost/blog'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = '123'

config_options ={"production":ProdConfig,"default":DevConfig}

