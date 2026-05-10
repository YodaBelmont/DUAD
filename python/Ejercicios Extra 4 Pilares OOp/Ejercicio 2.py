from abc import ABC, abstractmethod


class User(ABC):
    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(permission):
        pass


class AdminUser(User):
    def __init__(self, user):
        self.user = user
        self.role = "Admin"

    def get_role(self):
        return print(f"THIS USER HAS {self.role} ROLE")

    def has_permission(self, permission):
        if self.role == permission:
            return True
        return False


class RegularUser(User):
    def __init__(self, user):
        self.user = user
        self.role = "Read"

    def get_role(self):
        return print(f"THIS USER HAS {self.role} ROLE")

    def has_permission(self, permission):
        if self.role == permission:
            return True
        return False
