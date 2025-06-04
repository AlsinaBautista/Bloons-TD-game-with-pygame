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
        return self.rect.collidepoint(mouse_pos)
    
    def draw(self, screen):
        pygame.draw.circle(screen, c.BROWN, self.pos, self.radius)
        screen.blit(self.img, self.rect)