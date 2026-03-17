class Rectangle:

    def __init__(self, width, height):
        while True:
            if width >= 0 and height >= 0:
                self.width = width
                self.height = height
                break
            raise ValueError("VALUES MUST BE POSITIVE")

    def get_area(self):
        res = self.height * self.width
        print(res)
        return res

    def get_perimeter(self):
        res = (2 * self.height) + (2 * self.width)
        print(res)
        return res


rectangle1 = Rectangle(250, -300)

rectangle1.get_area()
rectangle1.get_perimeter()
