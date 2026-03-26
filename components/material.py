import numpy as np
from .ray import Ray

class Material:
    def eval(self, scene, hit, eye):
        raise NotImplementedError


class PhongMaterial(Material):
    def __init__(self, ambient, diffuse, specular, shininess):
        self.ambient = np.array(ambient)
        self.diffuse = np.array(diffuse)
        self.specular = np.array(specular)
        self.shininess = shininess

    def eval(self, scene, hit, eye):
        color = self.ambient * scene.ambient_light
        p = hit.pos
        n = self.normalize(hit.normal)
        v = self.normalize(eye - p)
        for light in scene.lights:
            Li, l = light.radiance(scene, p)
            shadow_ray = Ray(p + 1e-5 * l, l)
            shadow_hit = scene.compute_intersection(shadow_ray)
            if shadow_hit is not None:
                continue
            if np.dot(n, l) > 0:
                color += self.diffuse * Li * np.dot(n, l)
                r = self.reflect(-l, n)
                color += self.specular * Li * max(0, np.dot(r, v))**self.shininess
        return color

    def reflect(self, d, n):
        return d - 2 * np.dot(d, n) * n

    def normalize(self, v):
        return v / np.linalg.norm(v)