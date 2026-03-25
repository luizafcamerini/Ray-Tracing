from pydantic import BaseModel

class Position(BaseModel):
    x: float
    y: float
    z: float
    w: float = 0.0