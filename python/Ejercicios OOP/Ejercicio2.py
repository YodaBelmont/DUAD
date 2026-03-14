class Bus:
    def __init__(self):
        self.max_passengers = 40
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) >= self.max_passengers:
            print("NO SEATS AVAILABLE")
            return
        if not isinstance(person, Person):
            print("ONLY REAL PASSENGERS CAN ABOARD THE BUS")
            return
        self.passengers.append(person)
        print("PASSENGER ADDED")
        print(f"WELCOME ABOARD: {person.name}")

    def del_passenger(self, person):
        self.passengers.pop(person)
        print("PASSENGER DELETED:")
        print(self.passengers.pop(person))


class Person:
    def __init__(self, name):
        self.name = name


bus1 = Bus()
person1 = Person("Esteban")

bus1.add_passenger(person1)
