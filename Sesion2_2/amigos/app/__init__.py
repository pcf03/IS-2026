from flask import Flask, render_template
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # <- NUEVO IMPORT[cite: 40]
from config import app_config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/amigos')
    def tabla_amigos():
        from app.models import Amigo
        amigos = Amigo.query.all()
        return render_template('tabla_amigos.html', amigos=amigos)

    migrate = Migrate(app, db) # INICIALIZAR MIGRACIONES
    from app import models       # IMPORTAR MODELO

    return app