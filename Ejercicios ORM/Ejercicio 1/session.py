from sqlalchemy import select
from sqlalchemy.orm import Session
from models import User
from models import Address
from models import Car


def create_user(engine, name, email):
    with Session(engine) as session:
        new_user = User(
            name=name,
            email=email
        )
        session.add(new_user)
        session.commit()
        return new_user.id


def get_all_users(engine):
    with Session(engine) as session:
        query = select(User)
        
        users = session.scalars(query).all()
        for user in users:
            print(user.id, user.name, user.email)


def create_car(engine, brand, model, year):
    with Session(engine) as session:
        new_car = Car(
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


def insert_new_address(engine, state, address, postal_code):
    with Session(engine) as session:
        new_address = Address(
            state=state,
            address=address,
            postal_code=postal_code
        )
        session.add(new_address)
        session.commit()


def get_all_addresses(engine):
    with Session(engine) as session:
        query = select(Address)
        
        addresses = session.scalars(query).all()
        for address in addresses:
            print(address.id, address.state, address.address, address.postal_code)