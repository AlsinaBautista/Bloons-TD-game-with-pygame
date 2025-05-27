import pygame

RED = (245,48,18)
WHITE = (255, 255, 255)
BROWN = (136,86,0)
WIDTH = 1000
HEIGHT = 532
INVENTORY_WIDTH = int(WIDTH * 0.2) # La tienda ocupa el 20% del ancho total
CELD = 59
ENEMY_PATH = path = [
    (0, 265),   # Inicio fuera de pantalla (izquierda)
    (29, 265),     
    (265, 265),
    (265, 147),
    (383, 147),
    (383, 383),
    (265, 383),
    (265, 501),
    (619, 501),
    (619, 442),
    (678, 442),
    (678, 383),
    (737, 383),
    (737, 206),
    (560, 206),
    (560,  88),
    (501,  88),
    (501,  0)
]

ENEMY_HEALTH = 1
ENEMY_IMG = pygame.image.load("imgs/bloon.png")
ENEMY_SPEED = 100
ENEMY_POS = (0, 265)

