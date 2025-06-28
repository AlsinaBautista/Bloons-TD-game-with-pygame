import pygame
import constantes as c

class Map:
    def __init__(self, background_path):
        self.background = pygame.image.load(background_path).convert()

    def draw_background(self, screen):
        """
        Draw the background image on the screen.
        Blits the background image onto the screen at the top-left corner.
        -------------------------------------------------------------------------
        Arguments:
            screen (pygame.Surface): The surface on which to draw the background.
        -------------------------------------------------------------------------
        Returns:
            None
        """
        screen.blit(self.background, (0, 0))

    def draw_celds_border(self, screen, color, celd_size):
        """
        Draw the grid lines on the screen.
        Draws vertical and horizontal lines to create a grid effect.
        -------------------------------------------------------------------------
        Arguments:
            screen (pygame.Surface): The surface on which to draw the grid lines.
            color (tuple): The color of the grid lines in RGB format.
            celd_size (int): The size of each cell in the grid.
        -------------------------------------------------------------------------
        Returns:
            None
        """
        for x in range(0, screen.get_width() - c.INVENTORY_WIDTH, celd_size):
            pygame.draw.line(screen, color, (x, 0), (x, screen.get_height()))
        for y in range(0, screen.get_height(), celd_size):
            pygame.draw.line(screen, color, (0, y), (screen.get_width() - c.INVENTORY_WIDTH, y))
    
    def draw_celds(self, screen, grid, dragging_tower):
        """
        Draw the grid cells on the screen.
        Iterates through the grid and draws each cell with a specific color
        based on the value in the grid. It also handles the case where the mouse is dragging a tower.
        -------------------------------------------------------------------------
        Arguments:
            screen (pygame.Surface): The surface on which to draw the grid cells.
            grid (list): A 2D list representing the grid, where each cell contains a value.
            dragging_tower (Tower): The tower object being dragged, used to determine cell colors.
        -------------------------------------------------------------------------
        Returns:
            None
        """
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
                if not dragging_tower.water:
                    color = c.TRANS if value != 0 else c.GREY
                elif dragging_tower.water:
                    color = c.TRANS if value != 2 else c.GREY
                
                rect = pygame.Rect(0, 0, c.CELD, c.CELD)
                celd_surface = pygame.Surface((c.CELD, c.CELD), pygame.SRCALPHA)
                pygame.draw.rect(celd_surface, color, rect)
                screen.blit(celd_surface, (x, y))