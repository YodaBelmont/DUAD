from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from models import User

class UserSession():
    def __init__(self, engine):
        self.engine = engine
    
    
    def create_user(self, name, email):
        with Session(self.engine) as session:
            new_user = User(
                name=name,
                email=email
            )
            session.add(new_user)
            session.commit()
            return new_user.id


    def get_all_users(self):
        with Session(self.engine) as session:
            query = select(User)
            
            users = session.scalars(query).all()
            for user in users:
                print(user.id, user.name, user.email)


    def edit_user(self, **kwargs):
        with Session(self.engine) as session:
            
            if "id" not in kwargs:
                raise Exception("You must provide user id value")
            
            user = session.get(User, kwargs["id"])
            
            if not user:
                raise Exception("User not found")
            
            query = update(User).where(User.id == kwargs["id"])
            
            if "name" in kwargs:
                query = query.values(name=kwargs["name"])
            if "email" in kwargs:
                query = query.values(email=kwargs["email"])
            
            session.execute(query)
            session.commit()


    def delete_user(self, user_id):
        with Session(self.engine) as session:
            
            user = session.get(User, user_id)
            
            if not user:
                raise Exception("User not found")
            
            query = delete(User).where(User.id == user_id)
            session.execute(query)
            session.commit()