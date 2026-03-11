import math


class Circle:

    def __init__(self, radius):
        self.radius = int(radius)

    def get_area(self):
        area = math.pi * self.radius**2
        print(area)


circle1 = Circle(5)

circle1.get_area()
