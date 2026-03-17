class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Makes a sound"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return print("Guau")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return print("Miau")


dog1 = Dog("Esteban")
cat1 = Cat("Tomas")

dog1.speak()
cat1.speak()
