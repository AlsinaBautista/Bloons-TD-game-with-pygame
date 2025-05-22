import pygame

marron = (207, 168, 19)
white = (255, 255, 255)
width = 826
height = 532
celd = 54


enemy_path = path = [
    (0, 230),     # Inicio fuera de pantalla (izquierda)
    (250, 230),
    (250, 90),
    (420, 90),
    (420, 370),
    (230, 370),
    (230, 490),
    (670, 490),
    (670, 300),
    (500, 300),
    (500, 210),
    (690, 210),
    (690, 20),
    (500, 20),
    (500, 0)
]
enemy_health = 50
enemy_img = pygame.image.load("imgs/bloon.png")
enemy_speed = 0.2
enemy_pos = (0, 230)

