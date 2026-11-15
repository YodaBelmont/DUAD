from db_manager import DbManager
from session import (create_car, create_user, insert_new_address, get_all_addresses, get_all_cars, get_all_users)

def main():
    db_manager = DbManager()
    
    db_manager.create_tables()
    
    engine = db_manager.engine
    
    
    user_id = create_user(engine, "Juancho", "juancochor@mail.com")
    create_car(engine, "Toyota", "Corolla", 2000, user_id)
    insert_new_address(engine, user_id,  "Alajuela", "Naranjo", 20605)
    
    get_all_users(engine)
    get_all_cars(engine)
    get_all_addresses(engine)
    
    db_manager.disconnect()


if __name__ == "__main__":
    main()