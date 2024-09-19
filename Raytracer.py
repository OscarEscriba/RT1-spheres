import pygame
from pygame.locals import *
from gl import *
from Figures import *
from Material import Material
from Lights import *

width = 512
height = 512

screen = pygame.display.set_mode((width, height), pygame.SCALED)
clock = pygame.time.Clock()

rt = Raytracer(screen)

# Materiales
brick = Material(difuse=[1, 1, 1], spec=32, ks=0.1)  # Color blanco para el muñeco
black = Material(difuse=[0, 0, 0], spec=32, ks=0.1)  # Color negro para los botones y ojos
orange = Material(difuse=[1, 0.5, 0], spec=32, ks=0.1)  # Color anaranjado
gray = Material(difuse=[0.5, 0.5, 0.5], spec=32, ks=0.1)  # Color gris para el sombrero



# Luces 
rt.lights.append(DirectionalLight(direction=[-1, -1, -1], intensity=0.8))
rt.lights.append(DirectionalLight(direction=[0.5, -0.5, -1], intensity=0.8, color=[1, 1, 1]))
rt.lights.append(AmbientLight(intensity=0.1))

# Crear el muñeco de nieve
# Esferas del muñeco de nieve
rt.scene.append(Sphere([0, 0.35, -2], radius=0.25, material=brick))  # Cuerpo inferior
rt.scene.append(Sphere([0, -0.1, -2], radius=0.30, material=brick))  # Cuerpo medio
rt.scene.append(Sphere([0, -0.6, -2], radius=0.40, material=brick))  # Cabeza, ajustada a la posición correcta

#esfera para los botones
rt.scene.append(Sphere([0, 0 ,-1], radius=0.025, material=black))
rt.scene.append(Sphere([0, -0.1 ,-1], radius=0.025, material=black))
rt.scene.append(Sphere([0, -0.2 ,-1], radius=0.025, material=black))

#esferas para los ojos...
rt.scene.append(Sphere([-0.035, 0.26 ,-1], radius=0.02, material=black)) #si no cambiar a 0.025 y ahi dejar el radius.
rt.scene.append(Sphere([0.035, 0.26 ,-1], radius=0.02, material=black))

#esfera para la nariz...
rt.scene.append(Sphere([0, 0.22 ,-1], radius=0.02, material=orange))

# Boca (3 esferas)
rt.scene.append(Sphere([-0.04, 0.15, -1], radius=0.02, material=black))  # Diente izquierdo
rt.scene.append(Sphere([0, 0.15, -1], radius=0.02, material=black))       # Diente central
rt.scene.append(Sphere([0.04, 0.15, -1], radius=0.02, material=black))  # Diente derecho



rt.glRender()

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
