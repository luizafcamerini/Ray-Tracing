import numpy as np
from .ray import Ray
from .hit import Hit

class Shape():
    def __init__(self, pos):
        self.pos = pos


class Sphere(Shape):
    def __init__(self, center, radius, material):
        self.center = np.array(center)
        self.radius = radius
        self.material = material

    def intersect(self, ray: Ray):
        oc = ray.origin - self.center

        a = np.dot(ray.direction, ray.direction)
        b = 2.0 * np.dot(oc, ray.direction)
        c = np.dot(oc, oc) - self.radius**2

        discriminant = b**2 - 4*a*c

        if discriminant < 0:
            return None

        t = (-b - np.sqrt(discriminant)) / (2.0 * a)

        if t < 0:
            return None

        pos = ray.at(t)
        normal = (pos - self.center) / self.radius

        hit = Hit(
            t=t,
            pos=pos,
            normal=normal,
            material=self.material
        )

        hit.set_face_normal(ray.direction)
        return hit

class Plane(Shape):
    def __init__(self, point, normal, material):
        self.point = np.array(point)
        self.normal = self.normalize(np.array(normal))
        self.material = material

    def intersect(self, ray: Ray):
        denom = np.dot(self.normal, ray.direction)

        if abs(denom) < 1e-6:
            return None

        t = np.dot(self.point - ray.origin, self.normal) / denom

        if t < 0:
            return None

        pos = ray.at(t)

        hit = Hit(t=t, pos=pos, normal=self.normal, material=self.material)
        hit.set_face_normal(ray.direction)

        return hit

    def normalize(self, v):
        return v / np.linalg.norm(v)