from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config

# Importaciones para Prometheus (Sección 7)
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # Blueprint para HTML
    from .html import html as html_blueprint
    app.register_blueprint(html_blueprint, url_prefix='/html')
    
    # Blueprint para la API
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    
    # Blueprint para Health Check
    from .health import health as health_blueprint
    app.register_blueprint(health_blueprint)
    
    # Importante para que Flask-Migrate reconozca el modelo
    from app import models
    
    # Añado el middleware de Prometheus
    # Esto envuelve la aplicación original y abre la ruta secreta /metrics
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/metrics': make_wsgi_app()
    })
    
    return app