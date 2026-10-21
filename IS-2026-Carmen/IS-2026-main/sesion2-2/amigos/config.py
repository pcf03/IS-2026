# Configuraciones para distintas formas de lanzar la aplicación

class Config:
    "Clase base de la que derivarán las demás"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    "Configuración de desarrollo"
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    "Configuración de producción"
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}