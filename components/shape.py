from .position import Position

class Shape():
    def __init__(pos):
        self.pos = pos


class Sphere(Shape):
    def __init__(center: tuple, radius: tuple, pos: Position):
        self.center = center
        self.radius = radius