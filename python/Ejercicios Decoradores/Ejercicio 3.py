from datetime import date


def validate_user(func):
    def wrapper(user, *args, **kwargs):
        if not user.age >= 18:
            raise Exception("USER MUST BE AT LEAST 18 YEARS OLD")

        func(user, *args, **kwargs)

    return wrapper


class User:
    def __init__(self, date_of_birth, full_name):
        self.full_name = full_name
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )

    @validate_user
    def change_name(self):
        self.full_name = input("ENTER NEW FULL NAME: ")


user1 = User(date(2003, 1, 26), "Esteban Matamoros")
user1.change_name()
