from flask import Flask, request
from pg_manager import PgManager
from user_car_rent_repository import UserCarRentRepository

app = Flask(__name__)


db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="dolanpls23",
    host="localhost")

user_car_rent_repo = UserCarRentRepository(db_manager)


@app.route("/car_rent")
def get_rent_data():
    filters = request.args.to_dict()
    results = user_car_rent_repo.get_all(filters)
    return results


@app.route("/car_rent", methods=["POST"])
def register_new_rent_data():
    values = request.json
    result = user_car_rent_repo.register_new_rent(values)
    
    if not result:
        return {"An error has occurred": values}, 400
    
    return {"Rent data registered successfully": values}, 201


@app.route("/car_rent", methods=["PATCH"])
def complete_rent():
    values = request.json
    result = user_car_rent_repo(values)
    
    if not result:
        return {"An error has occurred": values}, 400
    
    return {"Rent data registered successfully": values}, 201


@app.route("/rent_status", methods=["PATCH"])
def complete_rent():
    values = request.json
    result = user_car_rent_repo(values)
    
    if not result:
        return {"An error has occurred": values}, 400
    
    return {"Rent data registered successfully": values}, 201




if __name__ == "__main__":
    app.run(debug=True)