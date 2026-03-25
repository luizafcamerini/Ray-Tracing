from pydantic import BaseModel

class Vector(BaseModel):
    x: float
    y: float
    z: float
    w: float = 1.0


class NormalVector(Vector):
    pass