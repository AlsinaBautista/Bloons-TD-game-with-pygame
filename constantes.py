import pygame

RED = (245,48,18)
WHITE = (255, 255, 255)
WIDTH = 1000
HEIGHT = 532
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
GRID_ROWS = HEIGHT // CELD
GRID_COLS = WIDTH // CELD
GRID = [[0 for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

for i in range(len(ENEMY_PATH) - 1):
    x1, y1 = ENEMY_PATH[i]
    x2, y2 = ENEMY_PATH[i + 1]
    col1, row1 = x1 // CELD, y1 // CELD
    col2, row2 = x2 // CELD, y2 // CELD

    if row1 == row2:
        for col in range(min(col1, col2), max(col1, col2) + 1):
            GRID[row1][col] = 1
    elif col1 == col2:
        for row in range(min(row1, row2), max(row1, row2) + 1):
            GRID[row][col1] = 1


ENEMY_HEALTH = 1
ENEMY_IMG = pygame.image.load("imgs/bloon.png")
ENEMY_SPEED = 100
ENEMY_POS = (0, 265)

