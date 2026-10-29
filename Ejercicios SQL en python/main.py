from pg_manager import PgManager
from user_repository import UserRepository


db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="dolanpls23",
    host="localhost")

users_repo = UserRepository(db_manager)


#users_repo.create_user("Rodolfo Tomas", "fofito@mail.com", "rodolfo", "rdlf12345", "1995-01-15", "inactive")

#users_repo.change_user_status(52, "active")