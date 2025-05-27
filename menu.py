import pygame

class Menu:
    def __init__(self):
        self.boton_rect = pygame.Rect(305, 330, 370, 140)

    def dibujar_boton(self, superficie, mouse_pos):
        # Crear una superficie con canal alfa
        boton_surface = pygame.Surface((self.boton_rect.width, self.boton_rect.height), pygame.SRCALPHA)

        # Detectar si el mouse esta sobre el boton
        if self.boton_rect.collidepoint(mouse_pos):
            color = (0, 0, 0, 80)  # Color semitransparente en hover
        else:
            color = (0, 0, 0, 0)   # Totalmente transparente

        # Dibujar rectangulo con esquinas redondeadas
        pygame.draw.rect(boton_surface, color, boton_surface.get_rect(), border_radius=30)

        # Dibujar el boton sobre la superficie principal
        superficie.blit(boton_surface, (self.boton_rect.x, self.boton_rect.y))
