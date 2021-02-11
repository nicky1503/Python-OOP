from math import sqrt


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def set_x(self, new_x: float):
        self.x = new_x

    def set_y(self, new_y: float):
        self.y = new_y

    def distance(self, x: int, y: int):
        return sqrt((self.x - x)**2 + (self.y - y)**2)


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))




