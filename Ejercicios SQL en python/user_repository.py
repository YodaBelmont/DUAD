class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def _format_user(self, users):
        return{
            "id": users[0],
            "name": users[1],
            "email": users[2],
            "username": users[3],
            "password": users[4],
            "birthDate": users[5],
            "accountStatus": users[6]
        }
    
    def get_all(self):
        try:
            results = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.Users")
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all users from database:", error)
            return False
    
    def create_user(self, name, email, username, password, birth_date, account_status):
        try:
            self.db_manager.execute_query("INSERT INTO lyfter_car_rental.Users(name, email, username, password, birth_date, account_status) VALUES (%s, %s, %s, %s, %s, %s)",(name, email, username, password, birth_date, account_status))
            print("User created successfully")
            return True
        except Exception as error:
            print("Error creating new user:", error)
            return False
    
    def change_user_status(self, user_id, new_status):
        try:
            self.db_manager.execute_query("UPDATE lyfter_car_rental.Users SET account_status = %s WHERE id = %s", (new_status, user_id))
            print("User updated successfully")
            return True
        except Exception as error:
            print("Error changing user status:", error)
            return False
    
    def flag_user(self, user_id):
        try:
            self.db_manager.execute_query("UPDATE lyfter_car_rental.Users SET account_status = %s WHERE id = %s", ("debtor", user_id))
            print("User flagged successfully")
            return True
        except Exception as error:
            print("Error flagging user:", error)
            return False
    
    def get_by_username(self, username):
        try:
            results = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.Users WHERE username = %s",(username))
            formatted_result = self._format_user(results)
            return formatted_result
        except Exception as error:
            print("Error finding user:", error)
            return False