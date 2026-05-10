class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @property
    def name(self):
        return self.__name

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("SALARY CANNOT BE A NEGATIVE VALUE")
        self.__salary = value

    def increase_salary(self, increase):
        if increase < 0:
            raise ValueError("VALUE CANNOT BE NEGATIVE")
        self.__salary *= increase
