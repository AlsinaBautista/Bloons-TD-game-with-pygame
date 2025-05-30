import pygame
import constantes as c

class Map:
    def __init__(self, background_path):
        self.background = pygame.image.load(background_path).convert()

    def draw_background(self, screen):
        screen.blit(self.background, (0, 0))

    def draw_celds_border(self, screen, color, celd_size):
        for x in range(0, screen.get_width() - c.INVENTORY_WIDTH, celd_size):
            pygame.draw.line(screen, color, (x, 0), (x, screen.get_height()))
        for y in range(0, screen.get_height(), celd_size):
            pygame.draw.line(screen, color, (0, y), (screen.get_width() - c.INVENTORY_WIDTH, y))
    
    def draw_celds(self, screen, grid):
        for row_idx, row in enumerate(grid):
            for col_idx, value in enumerate(row):
                x = col_idx * c.CELD
                y = row_idx * c.CELD
                
                # No dibujar en la zona del inventario a la derecha
                if x >= screen.get_width() - c.INVENTORY_WIDTH:             
                    rect = pygame.Rect(0, 0, x - (screen.get_width() - c.INVENTORY_WIDTH), c.CELD)
                    celd_surface = pygame.Surface((c.CELD, c.CELD), pygame.SRCALPHA)
                    pygame.draw.rect(celd_surface, color, rect)
                    screen.blit(celd_surface, (x - (screen.get_width() - c.INVENTORY_WIDTH), y))
                    continue
                
                # Elegir color según el valor
                color = c.TRANS_RED if value != 0 else c.TRANS_GREEN
                
                rect = pygame.Rect(0, 0, c.CELD, c.CELD)
                celd_surface = pygame.Surface((c.CELD, c.CELD), pygame.SRCALPHA)
                pygame.draw.rect(celd_surface, color, rect)
                screen.blit(celd_surface, (x, y))