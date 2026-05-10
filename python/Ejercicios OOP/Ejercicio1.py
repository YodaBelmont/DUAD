import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * self.radius**2
        return area


circle1 = Circle(5)

print(circle1.get_area())
