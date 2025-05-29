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
        pygame.draw.circle(screen, c.BROWN, self.pos, self.radius)
        screen.blit(self.image, self.rect)
    
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
    def change_speed(self):
        self.speedup = not self.speedup #Esta linea alterna entre true y false, si estaba en true pasa a false y viceversa
        if self.speedup: #Si speedup es True, devuelvo 2, si es False, devuelvo 1
            return 2
        else:
            return 1
    
    def hover(self, surface, mouse_pos):
        boton_surface = pygame.Surface((self.boton_rect.width, self.boton_rect.height), pygame.SRCALPHA)

        # Detectar si el mouse esta sobre el boton
        if self.boton_rect.collidepoint(mouse_pos):
            color = (0, 0, 0, 80)  # Color semitransparente en hover
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            color = (0, 0, 0, 0)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # Dibujar rectangulo con esquinas redondeadas
        pygame.draw.rect(boton_surface, color, boton_surface.get_rect(), border_radius=30)

        # Dibujar el boton sobre la superficie principal
        surface.blit(boton_surface, (self.boton_rect.x, self.boton_rect.y))
    
    
