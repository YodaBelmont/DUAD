from flask import Flask, request
from pg_manager import PgManager
from user_repository import UserRepository

app = Flask(__name__)


db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="dolanpls23",
    host="localhost")

users_repo = UserRepository(db_manager)

@app.route("/users")
def get_users():
    filters = request.args.to_dict()
    results = users_repo.get_all(filters)
    return results


@app.route("/user", methods=["POST"])
def create_user():
    params = request.json
    user = users_repo.create_user(params)
    if not user:
        return {"error":"An error has occurred"}, 400
    
    return {"User created":user}, 201


@app.route("/user", methods=["PATCH"])
def change_status():
    values = request.json
    result = users_repo.change_user_status(values)
    
    return {"user status modified":result}, 201


@app.route("/user", methods=["PATCH"])
def flag_user():
    values = request.json
    result = users_repo.flag_user(values)
    
    return {"user flagged": result}, 201 



if __name__ == "__main__":
    app.run(debug=True)