class Config:
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = '123'

config_options ={"production":ProdConfig,"default":DevConfig}

