from .users import users
from .main import main

def register_blueprints(app):
    app.register_blueprint(users)
    app.register_blueprint(main)