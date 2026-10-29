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
    
    def complete_rent(self, user_id, car_id, ):
        try:
            self.db_manager.execute_query("UPDATE lyfter_car_rental.User_car_rent SET state = 'completed' WHERE car_id = %s AND user_id = %s", (car_id, user_id))
            print("Rent status set to complete")
            return True
        except Exception as error:
            print("Error completing car rent:", error)
    
    def change_rent_status(self, user_id, car_id, new_status):
        try:
            self.db_manager.execute_query("UPDATE lyfter_car_rental.User_car_rent SET state = %s WHERE car_id = %s AND user_id = %s", (new_status, car_id, user_id))
            print("Rent status updated successfully")
            return True
        except Exception as error:
            print("Error completing car rent:", error)
    
    def get_all(self):
        try:
            results = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.User_car_rent")
            formatted_results = [self._format_data(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting rent data from database:", error)
            return False
    
    def get_all_by_state(self, state):
        try:
            results = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.User_car_rent WHERE state = %s", (state))
            formatted_results = [self._format_data(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting rent data from database:", error)
            return False