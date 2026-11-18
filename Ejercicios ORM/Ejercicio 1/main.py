from db_manager import DbManager
from user_session import create_user, get_all_users
from car_session import create_car, get_all_cars
from address_session import insert_new_address, get_all_addresses


def main():
    db_manager = DbManager()
    
    db_manager.create_tables()
    
    engine = db_manager.engine
    
    
    user_id = create_user(engine, "Juancho", "juancochor@mail.com")
    create_car(engine, user_id, "Toyota", "Corolla", 2000)
    insert_new_address(engine, user_id,  "Alajuela", "Naranjo", 20605)
    
    get_all_users(engine)
    get_all_cars(engine)
    get_all_addresses(engine)
    
    db_manager.disconnect()


if __name__ == "__main__":
    main()