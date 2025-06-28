import pygame
import constantes as c
class Gen_But:
    def __init__(self, img, pos, radius):
        self.img = img
        self.pos = pos
        self.radius = radius
        self.rect = self.img.get_rect(center=pos)
        self.boton_rect = pygame.Rect(pos[0] - radius, pos[1] - radius, radius * 2, radius * 2)
    
    def is_clicked(self, mouse_pos):
        """
        Check if the button is clicked based on the mouse position.
        -------------------------------------------------------------------------
        Arguments:
            mouse_pos (tuple): The current position of the mouse.
        -------------------------------------------------------------------------
        Returns:
            bool: True if the button is clicked, False otherwise.
        """
        return self.rect.collidepoint(mouse_pos)
    
    def draw(self, screen):
        """
        Draw the button on the screen.
        Draws a circle and the button image at the specified position.
        -------------------------------------------------------------------------
        Arguments:
            screen (pygame.Surface): The surface on which to draw the button.
        -------------------------------------------------------------------------
        Returns:
            None
        """
        pygame.draw.circle(screen, c.BROWN, self.pos, self.radius)
        screen.blit(self.img, self.rect)