from flask import Blueprint, request
from pg_manager import PgManager
from cars_repository import CarRepository

cars_bp = Blueprint("cars", __name__)


db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="dolanpls23",
    host="localhost")

cars_repo = CarRepository(db_manager)

@cars_bp.route("/cars")
def get_cars():
    filters = request.args.to_dict()
    results = cars_repo.get_all(filters)
    return results, 200


@cars_bp.route("/car", methods=["POST"])
def create_car():
    params = request.json
    car = cars_repo.create_car(params)
    if not car:
        return {"error":"An error has occurred"}, 400
    
    return {"Car created":car}, 201


@cars_bp.route("/car", methods=["PATCH"])
def change_car_status():
    params = request.json
    car = cars_repo.change_car_status(params)
    if not car:
        return {"error":"An error has occurred"}, 404
    
    return {"Car status updated":car}, 200
