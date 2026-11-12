from flask import Flask

from user_api import users_bp
from cars_api import cars_bp
from user_car_rent_api import rents_bp

app = Flask(__name__)

app.register_blueprint(users_bp)
app.register_blueprint(cars_bp)
app.register_blueprint(rents_bp)

if __name__ == "__main__":
    app.run(debug=True)