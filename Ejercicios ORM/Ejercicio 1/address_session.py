from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from models import Address


def insert_new_address(engine, user_id, state, address, postal_code):
    with Session(engine) as session:
        new_address = Address(
            user_id=user_id,
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


def edit_address(engine, **kwargs):
    with Session(engine) as session:
        if "id" not in kwargs:
            raise Exception("You must provide address id value")
        
        address = session.get(Address, kwargs["id"])
        
        if not address:
            raise Exception("Address not found")
        
        query = update(Address).where(Address.id == kwargs["id"])
        
        if "user_id" in kwargs:
            query = query.values(user_id=kwargs["user_id"])
        if "state" in kwargs:
            query = query.values(state=kwargs["state"])
        if "address" in kwargs:
            query = query.values(address=kwargs["address"])
        if "postal_code" in kwargs:
            query = query.values(postal_code=kwargs["postal_code"])
        
        session.execute(query)
        session.commit()


def delete_address(engine, address_id):
    with Session(engine) as session:
        
        car = session.get(Address, address_id)
        
        if not car:
            raise Exception("Car not found")
        
        query = delete(Address).where(Address.id == address_id)
        session.execute(query)
        session.commit()