class CarRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def _format_car(self, cars):
        return{
            "id": cars[0],
            "brand": cars[1],
            "model": cars[2],
            "year": cars[3],
            "state": cars[4],
    }
    
    def create_car(self, car_json):
        try:
            
            valid_fields = ["brand", "model", "year", "state"]
            
            for field in valid_fields:
                if field not in car_json:
                    return False

            self.db_manager.execute_query("INSERT INTO lyfter_car_rental.Cars(brand, model, year, state) VALUES (%s, %s, %s, %s)",
                                        (car_json["brand"], car_json["model"], car_json["year"], car_json["state"]))
            print("User created successfully")
            return car_json
        except Exception as error:
            print("Error creating new user:", error)
            return False
    
    def change_car_status(self, values):
        try:
            valid_statuses = ["available", "rented", "maintenance"]
            
            if values["new_status"] not in valid_statuses:
                return False
            
            car = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.Cars WHERE id = %s", (values["id"],) )
            
            if car == None:
                return False
            
            self.db_manager.execute_query("UPDATE lyfter_car_rental.Cars SET state = %s WHERE id = %s", (values["new_status"], values["id"]))
            car = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.Cars WHERE id = %s", (values["id"],) )
            print("Car updated successfully")
            return car
        except Exception as error:
            print("Error changing car status:", error)
            return False
    
    def get_all(self, filters):
        try:
            query = "SELECT * FROM lyfter_car_rental.Cars"
            params = []
            query_elements = []
            
            if "brand" in filters:
                query_elements.append("brand = %s")
                params.append(filters["brand"])
            
            if "model" in filters:
                query_elements.append("model = %s")
                params.append(filters["model"])
            
            if "year" in filters:
                query_elements.append("year = %s")
                params.append(filters["year"])
            
            if "state" in filters:
                query_elements.append("state = %s")
                params.append(filters["state"])
            
            if params:
                query += " WHERE " + " AND ".join(query_elements)
            
            results = self.db_manager.execute_query(query, tuple(params))
            
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all users from database:", error)
            return False