import pygame

class Menu:
    def __init__(self):
        self.boton_rect = pygame.Rect(305, 330, 370, 140)

    def draw_button(self, surface, mouse_pos):
        """
        Draws a button on the given surface with rounded corners and hover effect.
        Creates a semi-transparent rectangle that changes color when the mouse hovers over it.
        -------------------------------------------------------------------------
        Arguments:
            surface (pygame.Surface): The surface on which to draw the button.
            mouse_pos (tuple): The current position of the mouse cursor.
        -------------------------------------------------------------------------
        Returns:
            None
        """
        # Crear una superficie con canal alfa
        botton_surface = pygame.Surface((self.boton_rect.width, self.boton_rect.height), pygame.SRCALPHA)

        # Detectar si el mouse esta sobre el boton
        if self.boton_rect.collidepoint(mouse_pos):
            color = (0, 0, 0, 80)  # Color semitransparente en hover
        else:
            color = (0, 0, 0, 0)   # Totalmente transparente

        # Dibujar rectangulo con esquinas redondeadas
        pygame.draw.rect(botton_surface, color, botton_surface.get_rect(), border_radius=30)

        # Dibujar el boton sobre la superficie principal
        surface.blit(botton_surface, (self.boton_rect.x, self.boton_rect.y))
