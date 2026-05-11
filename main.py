import numpy as np
from components.camera import Camera
from components.material import PhongMaterial
from components.scene import Scene
from components.shapes import Sphere, Plane, Box
from components.light import PointLight, AreaLight
from components.film import Film
from components.transform import Transform
from components.instance import Instance

scene = Scene()

# =========================
# ESFERA
# =========================
red_material = PhongMaterial(
    ambient=[0.1, 0.0, 0.0],
    diffuse=[0.7, 0.1, 0.1],
    specular=[1.0, 1.0, 1.0],
    shininess=50
)
sphere = Instance(
    Sphere(
        radius=0.5,
        center=[-1, 1, -3]
    ),
    red_material,
)
scene.add_object(sphere)

# =========================
# ELIPSE
# =========================
yellow_material = PhongMaterial(
    ambient=[0.1, 0.1, 0.0],
    diffuse=[0.7, 0.7, 0.1],
    specular=[1.0, 1.0, 1.0],
    shininess=50
)
elipse = Instance(
    Sphere(
        radius=0.5,
        center=[0, 1, -3]
    ),
    yellow_material,
    transform=Transform(
        scale=[0.5, 1, 1]
    )
)
scene.add_object(elipse)

# =========================
# CAIXA
# =========================
blue_material = PhongMaterial(
    ambient=[0.0, 0.0, 0.1],
    diffuse=[0.1, 0.1, 0.7],
    specular=[1.0, 1.0, 1.0],
    shininess=50
)
box = Instance(
    shape=Box(
        min_corner=[-0.5,-0.5,-0.5],
        max_corner=[0.5,0.5,0.5]
    ),

    material=blue_material,
    transform=Transform(
        translation=[1.5,1,-3],
        rotation=[10, 50, 60],
    )
)
scene.add_object(box)

# =========================
# PLANO
# =========================
gray_material = PhongMaterial(
    ambient=[0.2, 0.2, 0.2],
    diffuse=[0.7, 0.7, 0.7],
    specular=[0.3, 0.3, 0.3],
    shininess=15
)
plane = Instance(
    Plane(
        normal=[0, 1, 0],
        material=gray_material
    ),
    gray_material,
    transform=Transform(
        translation=[0, -0.5, 0]
    )
)
scene.add_object(plane)

# =========================
# LUZ
# =========================
light = AreaLight(
    position=[0, 4, -3],
    normal=[0, -1, 0],
    width=3,
    height=3,
    power=80,
    samples=25
)
scene.add_light(light)

# =========================
# CAMERA
# =========================
camera = Camera(
    eye=[0, 0.5, 2],
    center=[0, 0, -3],
    up=[0, 1, 0],
    fov=np.pi / 3,
    aspect=1.0
)

# =========================
# FILME
# =========================
film = Film(
    width=400,
    height=400,
    samples=64
)

# =========================
# MAIN LOOP
# =========================
for j in range(film.height):
    print(f"Rendering line {j+1}/{film.height}")
    for i in range(film.width):
        for light in scene.lights:
            if hasattr(light, 'reset_sample_index'):
                light.reset_sample_index()
        color = np.array([0.0, 0.0, 0.0])
        for _ in range(film.sample_count()):
            x, y = film.get_sample(i, j)
            ray = camera.generate_ray(x, y)
            color += scene.trace_ray(ray)
        color /= film.sample_count()
        film.set_pixel(i, j, color)

film.save("render.png")