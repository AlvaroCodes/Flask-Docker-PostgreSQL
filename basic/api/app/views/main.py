from flask import Blueprint

main = Blueprint("main", __name__, url_prefix="/")

@main.route("/", methods=["GET"])
def index():
    routes = [
        {
            "path": "/users",
            "methods": ["GET"],
            "description": "Get all users"
        },
        {
            "path": "/users/<int:id>",
            "methods": ["GET"],
            "description": "Get a user by ID"
        },
        {
            "path": "/users",
            "methods": ["POST"],
            "description": "Create a new user"
        },
        {
            "path": "/users/<int:id>",
            "methods": ["PUT"],
            "description": "Update a user by ID"
        },
        {
            "path": "/users/<int:id>",
            "methods": ["DELETE"],
            "description": "Delete a user by ID"
        }
    ]
    return routes

