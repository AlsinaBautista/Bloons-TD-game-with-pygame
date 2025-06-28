import pygame
import constantes as c
class UpBut:
    def __init__(self, height, width, img, pos):
        self.height = height
        self.width = width
        self.img = img
        self.pos = pos
        self.rect = self.img.get_rect(center=pos)
    
    def is_clicked(self, mouse_pos):
        """
        Check if the upgrade button is clicked based on the mouse position.
        -------------------------------------------------------------------------
        Arguments:
            mouse_pos (tuple): The current position of the mouse.
        -------------------------------------------------------------------------
        Returns:
            bool: True if the upgrade button is clicked, False otherwise.
        """
        return self.rect.collidepoint(mouse_pos)
    
    def draw(self, screen, upgrade_text, color):
        """
        Draw the upgrade button on the screen.
        This method blits the button image and renders the upgrade text on the screen.
        -------------------------------------------------------------------------
        Arguments:
            screen (pygame.Surface): The surface on which to draw the upgrade button.
            upgrade_text (str): The text to display on the upgrade button.
            color (tuple): The color of the text.
        -------------------------------------------------------------------------
        Returns:
            None
        """
        screen.blit(self.img, self.rect)
        font = pygame.font.Font("fonts/OETZTYP_.TTF", 14)
        text1 = font.render(str(upgrade_text), True, color)
        text_rect1 = text1.get_rect(center=(self.pos[0], self.rect.top + 35))
        text2 = font.render(str("UPGRADE"), True, color)
        text_rect2 = text2.get_rect(center=(self.pos[0], self.rect.top + 20))
        screen.blit(text1, text_rect1)
        screen.blit(text2, text_rect2)

    def is_hover(self, mouse_pos, screen):
        """
        Check if the mouse is hovering over the upgrade button and draw a semi-transparent rectangle if it
        is.
        -------------------------------------------------------------------------
        Arguments:
            mouse_pos (tuple): The current position of the mouse.
            screen (pygame.Surface): The surface on which to draw the hover effect.
        -------------------------------------------------------------------------
        Returns:
            bool: True if the mouse is hovering over the button, False otherwise.
        """
        boton_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        if self.rect.collidepoint(mouse_pos):
            color = (0, 0, 0, 80)  # Color semitransparente en hover
        else:
            color = (0, 0, 0, 0)
        pygame.draw.rect(boton_surface, color, boton_surface.get_rect(), border_radius=10)
        # Dibujar el boton sobre la superficie principal
        screen.blit(boton_surface, (self.rect.x, self.rect.y))
        return self.rect.collidepoint(mouse_pos)
        
"""boton_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
# Detectar si el mouse esta sobre el boton
if self.rect.collidepoint(mouse_pos):
    color = (0, 0, 0, 80)  # Color semitransparente en hover
    pygame.mouse.set_cursor(hand)
else:
    color = (0, 0, 0, 0)
    pygame.mouse.set_cursor(cursor)
# Dibujar rectangulo con esquinas redondeadas
pygame.draw.rect(boton_surface, color, boton_surface.get_rect(), border_radius=10)
# Dibujar el boton sobre la superficie principal
surface.blit(boton_surface, (self.rect.x, self.rect.y))"""