import pygame
import constantes as c

class Button:

    def __init__(self, image, pos, radius):
        self.pos = pos
        self.radius = radius
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.boton_rect = pygame.Rect(pos[0] - radius, pos[1] - radius, radius * 2, radius * 2)
        self.speedup = False

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
        screen.blit(self.image, self.rect)
    
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
    
    def change_speed(self):
        """
        Change the speedup state of the button.
        -------------------------------------------------------------------------
        Returns:
            int: Returns 2 if speedup is True, otherwise returns 1.
        """
        self.speedup = not self.speedup #Esta linea alterna entre true y false, si estaba en true pasa a false y viceversa
        if self.speedup: #Si speedup es True, devuelvo 2, si es False, devuelvo 1
            return 2
        else:
            return 1
    
    def hover(self, surface, mouse_pos, cursor, hand):
        """
        Check if the mouse is hovering over the button and draw a semi-transparent rectangle if it is.
        -------------------------------------------------------------------------
        Arguments:
            surface (pygame.Surface): The surface on which to draw the hover effect.
            mouse_pos (tuple): The current position of the mouse.
            cursor (pygame.Surface): The cursor image to be displayed.
            hand (pygame.Surface): The hand image to be displayed when hovering.
        -------------------------------------------------------------------------
        Returns:
            bool: True if the mouse is hovering over the button, False otherwise.
        """
        return self.rect.collidepoint(mouse_pos)
    
    
