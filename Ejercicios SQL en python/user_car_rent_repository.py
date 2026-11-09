class UserCarRentRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_data(self, data):
        return{
            "id": data[0],
            "user_id": data[1],
            "car_id": data[2],
            "rental_date": data[3],
            "state": data[4],
    }
    
    def register_new_rent(self, values):
        try:
            car = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.Cars WHERE id = %s AND state = 'available'", (values["car_id"], ))
            
            if not car:
                return False
            
            self.db_manager.execute_query("INSERT INTO lyfter_car_rental.User_car_rent (user_id, car_id, state) VALUES (%s, %s, %s)", (values["user_id"], values["car_id"], values["state"]))
            self.db_manager.execute_query("UPDATE lyfter_car_rental.Cars SET state = 'rented' WHERE id = %s", (values["car_id"], ))
            print("New rent register created successfully")
            return True
        except Exception as error:
            print("There was a error creating new rent register:", error)
    
    def complete_rent(self, values):
        try:
            if "rent_id" not in values:
                return False
            
            rent = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.User_car_rent WHERE id = %s", (values["rent_id"], ))
            
            if not rent:
                return False
            
            car_id = rent[0][2]
            
            self.db_manager.execute_query("UPDATE lyfter_car_rental.User_car_rent SET state = 'completed' WHERE id = %s", (values["rent_id"], ))
            self.db_manager.execute_query("UPDATE lyfter_car_rental.Cars SET state = 'available' WHERE id = %s", (car_id, ))
            print("Rent status set to complete")
            return True
        except Exception as error:
            print("Error completing car rent:", error)
    
    def change_rent_status(self, values):
        try:
            if "new_status" not in values:
                return False
            
            if "rent_id" not in values:
                return False
            
            rent = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.User_car_rent WHERE id = %s", (values["rent_id"], ))
            
            if not rent:
                return False
            
            self.db_manager.execute_query("UPDATE lyfter_car_rental.User_car_rent SET state = %s WHERE id = %s", (values["new_status"], values["rent_id"]))
            print("Rent status updated successfully")
            return True
        except Exception as error:
            print("Error completing car rent:", error)
    
    def get_all(self, filters):
        try:
            query = "SELECT * FROM lyfter_car_rental.User_car_rent"
            params = []
            query_elements = []
            
            if "user_id" in filters:
                query_elements.append("user_id = %s")
                params.append(filters["user_id"])
            
            if "car_id" in filters:
                query_elements.append("car_id = %s")
                params.append(filters["car_id"])
            
            if "state" in filters:
                query_elements.append("state = %s")
                params.append(filters["state"])
            
            if params:
                query += " WHERE " + " AND ".join(query_elements)
            
            results = self.db_manager.execute_query(query, tuple(params))
            
            formatted_results = [self._format_data(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all rent data from database:", error)
            return False