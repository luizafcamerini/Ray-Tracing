class Hit():
    def __init__(t: tuple, pos: tuple, normal: tuple, backfacing: bool, light):
        self.t = t
        self.pos = pos
        self.normal = normal
        self.backfacing = backfacing
        self.light = light