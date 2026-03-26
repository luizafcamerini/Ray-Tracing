import numpy as np
from components.camera import Camera
from components.material import PhongMaterial
from components.scene import Scene
from components.shapes import Sphere, Plane
from components.light import PointLight
from components.film import Film

# =========================
# SETUP DA CENA
# =========================

scene = Scene()

#Esfera
red_material = PhongMaterial(
    ambient=[0.1, 0.0, 0.0],
    diffuse=[0.7, 0.1, 0.1],
    specular=[1.0, 1.0, 1.0],
    shininess=50
)
sphere = Sphere(center=[0, 0, -3], radius=1, material=red_material)
scene.add_object(sphere)

#Plano
gray_material = PhongMaterial(
    ambient=[0.1, 0.1, 0.1],
    diffuse=[0.5, 0.5, 0.5],
    specular=[0.2, 0.2, 0.2],
    shininess=10
)
plane = Plane(
    point=[0, -1, 0],
    normal=[0, 1, 0],
    material=gray_material
)
scene.add_object(plane)

#Luz
light = PointLight(
    pos=[0, 5, -3],
    power=20
)
scene.add_light(light)

# =========================
# CAMERA
# =========================

camera = Camera(
    eye=[0, 1, 2],
    center=[0, 0, -3],
    up=[0, 1, 0],
    fov=np.pi / 3,
    aspect=1.0
)

# =========================
# FILM (imagem)
# =========================

film = Film(width=400, height=400, samples=10)

# =========================
# MAIN LOOP
# =========================

for j in range(film.height):
    print(f"Rendering line {j+1}/{film.height}")
    for i in range(film.width):
        color = np.array([0.0, 0.0, 0.0])

        for _ in range(film.sample_count()):
            x, y = film.get_sample(i, j)
            ray = camera.generate_ray(x, y)
            color += scene.trace_ray(ray)

        color /= film.sample_count()
        film.set_pixel(i, j, color)

film.save("render.png")