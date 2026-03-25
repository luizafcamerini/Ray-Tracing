import numpy as np
from pydantic import BaseModel

class MatrixIdentity():
    """Represents a 4X4 identity matrix."""
    def __init__():
        self.matrix = np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
        ])

class MatrixTransform(BaseModel):
    matrix: np.array

class MatrixTransformNormal():
    def __init__(matrix: MatrixTransform):
        pass
