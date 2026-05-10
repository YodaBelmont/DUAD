class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return print(f"BRAND: {self._brand} YEAR: {self._year}")


class Car(Vehicle):
    def __init__(self, brand, year, doors, car_type):
        super().__init__(brand, year)
        self.doors = doors
        self.type = car_type

    def get_info(self):
        return print(
            f"BRAND: {self._brand} - YEAR: {self._year} - DOORS: {self.doors} - TYPE: {self.car_type}"
        )


class Motorcycle(Vehicle):
    def __init__(self, brand, year, motorcycle_type):
        super().__init__(brand, year)
        self.motorcycle_type = motorcycle_type

    def get_info(self):
        return print(
            f"BRAND: {self._brand} - YEAR: {self._year} - TYPE {self.motorcycle_type}"
        )
