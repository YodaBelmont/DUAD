# Sistema para manejar usuarios


class AuthMixin:
    def login(self, username, password):
        if username == self.username and password == self.password:
            return True
        return False


class PermMixin:
    def is_admin(self):
        return self.role == "Admin"


class User(AuthMixin, PermMixin):

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
