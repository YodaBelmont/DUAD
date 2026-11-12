from flask import Blueprint, request
from pg_manager import PgManager
from user_repository import UserRepository

users_bp = Blueprint("users", __name__)


db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="dolanpls23",
    host="localhost")

users_repo = UserRepository(db_manager)

@users_bp.route("/users")
def get_users():
    filters = request.args.to_dict()
    results = users_repo.get_all(filters)
    return results, 200


@users_bp.route("/user", methods=["POST"])
def create_user():
    params = request.json
    user = users_repo.create_user(params)
    if not user:
        return {"error":"An error has occurred"}, 400
    
    return {"User created":user}, 201


@users_bp.route("/user_status", methods=["PATCH"])
def change_status():
    values = request.json
    result = users_repo.change_user_status(values)
    
    if not result:
        return {"error":"An error has occurred"}, 404
    
    return {"user status modified":result}, 200


@users_bp.route("/flag_user", methods=["PATCH"])
def flag_user():
    values = request.json
    result = users_repo.flag_user(values)
    
    if not result:
        return {"error":"An error has occurred"}, 404
    
    return {"user flagged": result}, 200
