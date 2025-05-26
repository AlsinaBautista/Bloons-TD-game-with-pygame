import pygame

marron = (207, 168, 19)
white = (255, 255, 255)
width = 1000
height = 532
celd = 59
enemy_path = path = [
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
grid_rows = height // celd
grid_cols = width // celd
grid = [[0 for _ in range(grid_cols)] for _ in range(grid_rows)]

for i in range(len(enemy_path) - 1):
    x1, y1 = enemy_path[i]
    x2, y2 = enemy_path[i + 1]
    col1, row1 = x1 // celd, y1 // celd
    col2, row2 = x2 // celd, y2 // celd

    if row1 == row2:
        for col in range(min(col1, col2), max(col1, col2) + 1):
            grid[row1][col] = 1
    elif col1 == col2:
        for row in range(min(row1, row2), max(row1, row2) + 1):
            grid[row][col1] = 1


enemy_health = 1
enemy_img = pygame.image.load("imgs/bloon.png")
enemy_speed = 0.2
enemy_pos = (0, 265)

