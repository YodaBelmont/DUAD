from sqlalchemy import create_engine

class DbManager():    
    def __init__(self):
        self.db_uri = 'postgresql://postgres:dolanpls23@localhost:5432/postgres'
        self.engine = create_engine(self.db_uri, echo=True)
        self.connection = self.engine.connect()
        print("Connection successful")
    
    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
                print("Connection closed")
        except Exception as error:
            print("Connection failed:", error)