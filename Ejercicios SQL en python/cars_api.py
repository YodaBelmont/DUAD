from flask import Flask, request
from pg_manager import PgManager
from cars_repository import CarRepository

app = Flask(__name__)


db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="dolanpls23",
    host="localhost")

cars_repo = CarRepository(db_manager)

@app.route("/cars")
def get_cars():
    filters = request.args.to_dict()
    results = cars_repo.get_all(filters)
    return results


@app.route("/car", methods=["POST"])
def create_car():
    params = request.json
    car = cars_repo.create_car(params)
    if not car:
        return {"error":"An error has occurred"}, 400
    
    return {"Car created":car}, 201


@app.route("/car", methods=["PATCH"])
def change_car_status():
    params = request.json
    car = cars_repo.change_car_status(params)
    if not car:
        return {"error":"An error has occurred"}, 400
    
    return {"Car status updated":car}, 201


if __name__ == "__main__":
    app.run(debug=True)