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
    
    def hover(self, surface, mouse_pos, cursor, hand):
        return self.rect.collidepoint(mouse_pos)
    
    
