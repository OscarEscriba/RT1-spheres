import numpy as np
from gl import WHITE
import mathLibraries as ml

class Material(object):
    def __init__(self, diffuse=WHITE):
        self.diffuse = diffuse

class Intersect(object):
    def __init__(self, distance, point=None, normal=None, obj=None):
        self.distance = distance
        self.point = point       # Punto de intersección
        self.normal = normal     # Normal en el punto de intersección
        self.obj = obj           # Objeto intersectado (en este caso, la esfera)

class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        # P = O + t * D

        # Vector desde el origen del rayo al centro de la esfera
        L = ml.subVectors(self.center, orig)

        # Proyección del vector L en la dirección del rayo (tca es la proyección)
        tca = ml.dotProduct(L, dir)

        # Distancia desde el centro de la esfera hasta el punto más cercano en la dirección del rayo
        d2 = ml.dotProduct(L, L) - tca**2

        # Si la distancia es mayor que el radio de la esfera, no hay intersección
        if d2 > self.radius**2:
            return None

        # Calcular la distancia desde tca hasta los puntos de intersección
        thc = (self.radius**2 - d2) ** 0.5
        t0 = tca - thc
        t1 = tca + thc

        # Si ambas distancias son negativas, la esfera está detrás del origen del rayo
        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None

        # Calculamos el punto de intersección
        point = ml.addVectors(orig, ml.scalarMultiply(dir, t0))

        # Calculamos la normal en el punto de intersección
        normal = ml.subVectors(point, self.center)
        normal = ml.scalarMultiply(normal, 1 / np.linalg.norm(normal))  # Normalizar la normal

        # Devolvemos la intersección con toda la información
        return Intersect(distance=t0, point=point, normal=normal, obj=self)
