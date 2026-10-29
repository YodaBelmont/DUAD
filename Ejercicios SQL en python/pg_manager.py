import psycopg2

class PgManager:
    def __init__(self,db_name, user, password, host, port=5432):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        
        self.connection = self.create_connection(db_name, user, password, host, port)
        if self.connection:
            print("Connected to database")
            self.cursor = self.connection.cursor()
    
    def create_connection(self, db_name, user, password, host, port):
        try:
            connection = psycopg2.connect(
                host= host,
                port= port,
                user= user,
                password= password,
                dbname= db_name,
                )
            return connection
        except Exception as error:
            print("Error connecting to database: ", error)
            return None
    
    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")
    
    def execute_query(self, query, args=None):
        self.cursor.execute(query, args)
        self.connection.commit()
        
        if self.cursor.description:
            result = self.cursor.fetchall()
            return result
