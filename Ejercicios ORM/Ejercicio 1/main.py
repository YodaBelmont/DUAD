from db_manager import DbManager
from user_session import UserSession
from car_session import CarSession
from address_session import AddressSession


def main():
    db_manager = DbManager()
    db_manager.create_tables()
    
    engine = db_manager.engine
    user_session = UserSession(engine)
    car_session = CarSession(engine)
    address_session = AddressSession(engine)
    
    user_id = user_session.create_user("Juancho", "juancochor@mail.com")
    car_session.create_car(user_id, "Toyota", "Corolla", 2000)
    address_session.insert_new_address(user_id,  "Alajuela", "Naranjo", 20605)
    
    user_session.get_all_users()
    car_session.get_all_cars()
    address_session.get_all_addresses()
    
    db_manager.disconnect()


if __name__ == "__main__":
    main()