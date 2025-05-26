import pygame

class Money:

    def __init__(self, cant_inicial, image):
        self.cant_inicial = cant_inicial
        self.cant_total = cant_inicial
        self.img = image
        self.rect = image.get_rect(center=(20, 20))

    def add_money(self, cant):
        self.cant_total += cant

    def spend_money(self, cant):
        self.cant_total -= cant

    def get_money(self):
        return self.cant_total
    
    def draw(self, screen):
        screen.blit(self.img, self.rect)
        font = pygame.font.Font("fonts\OETZTYP_.TTF", 24)
        text = font.render(str(self.cant_total), True, (255, 255, 255))
        screen.blit(text, (self.rect.right + 10, self.rect.centery - 10))