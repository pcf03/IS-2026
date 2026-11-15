import os
# Definición de secretos a usar por la app
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite://")

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}