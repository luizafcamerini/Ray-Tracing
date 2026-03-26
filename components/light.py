import numpy as np
from .ray import Ray

class Light():
    def __init__(self, power: int):
        self.power = power


class PointLight(Light):
    def __init__(self, pos, power):
        super().__init__(power)
        self.pos = np.array(pos)

    def radiance(self, scene, p):
        l = self.pos - p
        l = l / np.linalg.norm(l)

        shadow_ray = Ray(p + 1e-5 * l, l)
        hit = scene.compute_intersection(shadow_ray)

        if hit is not None:
            return np.array([0, 0, 0]), np.array([0, 0, 0])

        r = np.linalg.norm(self.pos - p)
        Li = self.power / (r**2)

        return np.array([Li, Li, Li]), l