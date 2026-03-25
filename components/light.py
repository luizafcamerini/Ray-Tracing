class Light():
    def __init__(power: int):
        self.power = power


class PointLight(Light):
    def __init__(pos):
        self.pos = pos