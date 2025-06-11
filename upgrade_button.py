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
        return self.rect.collidepoint(mouse_pos)
    
    def draw(self, screen, upgrade_text):
        screen.blit(self.img, self.rect)
        font = pygame.font.Font("fonts/OETZTYP_.TTF", 24)
        text = font.render(str(upgrade_text), True, (255, 255, 255))
        screen.blit(text, (self.pos[0], self.pos[1] + 10))