from flask import Blueprint, request, jsonify
from app.models.user import User
from app.controllers.user import get_users_get, add_users_post, get_user_get, update_user_put, delete_user_delete
from app import db

users = Blueprint("users", __name__, url_prefix="/users")


@users.route("/", methods=["GET"])
def get_users():
    return jsonify(get_users_get())

@users.route("/", methods=["POST"])
def add_users():
    data = request.get_json()
    return jsonify(add_users_post(data, db))

@users.route("/<int:id>", methods=["GET"])
def get_user(id):
    user = get_user_get(id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
    
@users.route("/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    user = update_user_put(id, data, db)
    
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@users.route("/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = delete_user_delete(id, db)
    
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404