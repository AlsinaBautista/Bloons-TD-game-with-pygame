import pygame
import constantes as c

class Map:
    def __init__(self, background_path):
        self.background = pygame.image.load(background_path).convert()

    def draw_background(self, screen):
        screen.blit(self.background, (0, 0))

    def draw_celds(self, screen, color, celd_size):
        for x in range(0, screen.get_width(), celd_size):
            pygame.draw.line(screen, color, (x, 0), (x, screen.get_height()))
        for y in range(0, screen.get_height(), celd_size):
            pygame.draw.line(screen, color, (0, y), (screen.get_width(), y))

grid_rows = c.HEIGHT // c.CELD
grid_cols = c.WIDTH // c.CELD
grid = [[0 for _ in range(grid_cols)] for _ in range(grid_rows)]

for i in range(len(c.ENEMY_PATH) - 1):
    x1, y1 = c.ENEMY_PATH[i]
    x2, y2 = c.ENEMY_PATH[i + 1]
    col1, row1 = x1 // c.CELD, y1 // c.CELD
    col2, row2 = x2 // c.CELD, y2 // c.CELD

    if row1 == row2:
        for col in range(min(col1, col2), max(col1, col2) + 1):
            grid[row1][col] = 1
    elif col1 == col2:
        for row in range(min(row1, row2), max(row1, row2) + 1):
            grid[row][col1] = 1
grid[0][0] = 1
grid[0][1] = 1
grid[0][2] = 1
grid[0][-1] = 1
grid[0][-2] = 1
grid[0][-3] = 1
grid[0][-4] = 1
grid[1][-1] = 1
grid[1][0] = 1
grid[1][1] = 1
grid[1][-2] = 1
grid[2][-1] = 1
grid[2][0] = 1
grid[-1][0] = 1
grid[-1][1] = 1
grid[-1][2] = 1
grid[-2][0] = 1
grid[-2][1] = 1
grid[-3][0] = 1
grid[-1][-1] = 1
grid[-1][-2] = 1
grid[-1][-3] = 1
grid[-2][-1] = 1
grid[-2][-2] = 1
grid[-3][-1] = 1
grid[-4][-3] = 1
grid[-5][-3] = 1
grid[-3][-4] = 2
grid[-4][-4] = 2
grid[-5][-4] = 2
grid[-3][-5] = 2
grid[-4][-5] = 2
grid[-5][-5] = 2
grid[-3][-6] = 1
grid[-4][-6] = 1
