def init_database(app, db):
    from .user import User

    with app.app_context():
        db.create_all()