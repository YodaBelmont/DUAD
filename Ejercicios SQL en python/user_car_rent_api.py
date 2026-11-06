from flask import Blueprint, request
from pg_manager import PgManager
from user_car_rent_repository import UserCarRentRepository

rents_bp = Blueprint("rents", __name__)


db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="dolanpls23",
    host="localhost")

user_car_rent_repo = UserCarRentRepository(db_manager)


@rents_bp.route("/car_rent")
def get_rent_data():
    filters = request.args.to_dict()
    results = user_car_rent_repo.get_all(filters)
    return results


@rents_bp.route("/car_rent", methods=["POST"])
def register_new_rent_data():
    values = request.json
    result = user_car_rent_repo.register_new_rent(values)
    
    if not result:
        return {"An error has occurred": values}, 400
    
    return {"Rent data registered successfully": values}, 201


@rents_bp.route("/car_rent", methods=["PATCH"])
def complete_rent():
    values = request.json
    result = user_car_rent_repo.complete_rent(values)
    
    if not result:
        return {"An error has occurred": values}, 400
    
    return {"Rent data registered successfully": values}, 201


@rents_bp.route("/rent_status", methods=["PATCH"])
def change_rent_status():
    values = request.json
    result = user_car_rent_repo.change_rent_status(values)
    
    if not result:
        return {"An error has occurred": values}, 400
    
    return {"Rent data registered successfully": values}, 201
