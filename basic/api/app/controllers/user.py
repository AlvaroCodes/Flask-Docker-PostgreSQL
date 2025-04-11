from app.models.user import User

def get_users_get():
    all_users = User.query.all()
    user_model_sreilize = []

    if all_users:
        for user in all_users:
            user_model_sreilize.append(user.serialize())
    return user_model_sreilize


def add_users_post(data, db):
    user = User(data["username"], data["password"])

    db.session.add(user)
    db.session.commit()

    return user.serialize()

def get_user_get(id):
    user = User.query.get(id)
    if user:
        return user.serialize()
    else:
        return None
    

def update_user_put(id, data, db):
    user = User.query.get(id)
    
    if user:
        user.username = data["username"]
        user.password = data["password"]

        db.session.commit()
        return user.serialize()
    else:
        return None

def delete_user_delete(id, db):
    user = User.query.get(id)
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}
    else:
        return {"error": "User not found"}, 404 