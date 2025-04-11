from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    # 💾 Inicializa la base de datos
    db.init_app(app)

    # 🛢️ Registramos todos los blueprints desde la función
    from .views import register_blueprints
    register_blueprints(app)

    # 📦 Exportar los modelos a la bbdd
    # from .models import init_database
    # init_database(app, db)

    return app
