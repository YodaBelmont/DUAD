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
    
    def create_car(self, brand, model, year, state):
        try:
            self.db_manager.execute_query("INSERT INTO lyfter_car_rental.Cars(brand, model, year, state) VALUES (%s, %s, %s, %s)",(brand, model, year, state))
            print("Car created successfully")
            return True
        except Exception as error:
            print("Error creating new car:", error)
            return False
    
    def change_car_status(self, car_id, new_status):
        try:
            self.db_manager.execute_query("UPDATE lyfter_car_rental.Cars SET state = %s WHERE id = %s", (new_status, car_id))
            print("Car updated successfully")
            return True
        except Exception as error:
            print("Error changing car status:", error)
            return False
    
    def get_all(self):
        try:
            results = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.Cars")
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all cars from database:", error)
            return False
    
    def get_car_by_model(self, model):
        try:
            results = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.Cars WHERE model = %s", (model))
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all cars from database:", error)
            return False