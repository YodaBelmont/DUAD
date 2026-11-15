from sqlalchemy import create_engine
from models import Base


class DbManager():    
    def __init__(self):
        self.db_uri = 'postgresql://postgres:dolanpls23@localhost:5432/postgres'
        self.engine = create_engine(self.db_uri, echo=True)
        print("Connection successful")
    
    
    def create_tables(self):
        Base.metadata.create_all(self.engine)
        print("Tables created successfully")
    
    
    def disconnect(self):
        try:
            if self.connection:
                self.engine.dispose()
                print("Connection closed")
        except Exception as error:
            print("Connection failed:", error)