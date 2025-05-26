import pygame

marron = (207, 168, 19)
white = (255, 255, 255)
width = 1000
height = 532
celd = 59


enemy_path = path = [
    (0, 265),
    (29, 265),     # Inicio fuera de pantalla (izquierda)
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
enemy_health = 1
enemy_img = pygame.image.load("imgs/bloon.png")
enemy_speed = 0.2
enemy_pos = (0, 265)

