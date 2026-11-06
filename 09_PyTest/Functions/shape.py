import math

class shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimter(self):
        return 2* math.pi * self.radius