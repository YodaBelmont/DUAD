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
    
    def get_all(self, filters):
        try:
            query = "SELECT * FROM lyfter_car_rental.Users"
            params = []
            query_elements = []
            
            if "name" in filters:
                query_elements.append("name = %s")
                params.append(filters["name"])
            
            if "email" in filters:
                query_elements.append("email = %s")
                params.append(filters["email"])
            
            if "username" in filters:
                query_elements.append("username = %s")
                params.append(filters["username"])
            
            if "birth_date" in filters:
                query_elements.append("birth_date = %s")
                params.append(filters["birth_date"])
                
            if "account_status" in filters:
                query_elements.append("account_status = %s")
                params.append(filters["account_status"])
            
            if params:
                query += " WHERE " + " AND ".join(query_elements)
            
            results = self.db_manager.execute_query(query, tuple(params))
            
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all users from database:", error)
            return False
    
    def create_user(self, user_json):
        try:
            
            valid_fields = ["name", "email", "username", "password", "birth_date", "account_status"]
            
            for field in valid_fields:
                if field not in user_json:
                    return False
            
            if self.db_manager.execute_query("SELECT 1 FROM lyfter_car_rental.Users WHERE username = %s OR email = %s" , (user_json["username"], user_json["email"])):
                return False

            self.db_manager.execute_query("INSERT INTO lyfter_car_rental.Users(name, email, username, password, birth_date, account_status) VALUES (%s, %s, %s, %s, %s, %s)",
                                        (user_json["name"], user_json["email"], user_json["username"], user_json["password"], user_json["birth_date"], user_json["account_status"]))
            print("User created successfully")
            return user_json
        except Exception as error:
            print("Error creating new user:", error)
            return False
    
    def change_user_status(self, values):
        try:
            valid_statuses = ["active", "inactive"]
            
            if values["new_status"] not in valid_statuses:
                return False
            
            user = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.Users WHERE id = %s", (values["id"],) )
            
            if not user:
                return False
            
            self.db_manager.execute_query("UPDATE lyfter_car_rental.Users SET account_status = %s WHERE id = %s", (values["new_status"], values["id"]))
            user = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.Users WHERE id = %s", (values["id"],) )
            print("User updated successfully")
            return user
        except Exception as error:
            print("Error changing user status:", error)
            return False
    
    def flag_user(self, values):
        try:
            if "id" not in values:
                return False
            
            user = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.Users WHERE id = %s", (values["id"],) )
            
            if not user:
                return False
            
            self.db_manager.execute_query("UPDATE lyfter_car_rental.Users SET account_status = %s WHERE id = %s", ("debtor", values["id"]))
            print("User flagged successfully")
            return True
        except Exception as error:
            print("Error flagging user:", error)
            return False
