from models import Car
from models import User
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete


def create_car(engine, user_id, brand, model, year):
    with Session(engine) as session:
        new_car = Car(
            user_id=user_id,
            brand=brand,
            model=model,
            year=year
        )
        session.add(new_car)
        session.commit()


def get_all_cars(engine):
    with Session(engine) as session:
        query = select(Car)
        
        cars = session.scalars(query).all()
        for car in cars:
            print(car.id, car.brand, car.model, car.year)


def edit_car(engine, **kwargs):
    with Session(engine) as session:
        
        if "id" not in kwargs:
            raise Exception("You must provide car id value")
        
        car = session.get(Car, kwargs["id"])
        
        if not car:
            raise Exception("Car not found")
        
        query = update(Car).where(Car.id == kwargs["id"])
        
        if "user_id" in kwargs:
            query = query.values(user_id=kwargs["user_id"])
        if "brand" in kwargs:
            query = query.values(brand=kwargs["brand"])
        if "model" in kwargs:
            query = query.values(model=kwargs["model"])
        if "year" in kwargs:
            query = query.values(year=kwargs["year"])
        
        session.execute(query)
        session.commit()


def delete_car(engine, car_id):
    with Session(engine) as session:
        
        car = session.get(Car, car_id)
        
        if not car:
            raise Exception("Car not found")
        
        query = delete(Car).where(Car.id == car_id)
        session.execute(query)
        session.commit()


def associate_to_user(engine, user_id, car_id):
    with Session(engine) as session:
        car = session.get(Car, car_id)
        user = session.get(User, user_id)
        
        if not car:
            raise Exception("Car not found")
        
        if not user:
            raise Exception("User not found")
        
        query = update(Car).where(Car.id == car_id).values(user_id=user_id)
        session.execute(query)
        session.commit()