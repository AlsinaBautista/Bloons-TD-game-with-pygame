import pygame
from money import *

class Shop:
    def __init__(self, img_tower, x, y, price, money):
        self.img_tower = img_tower
        # Crear triangulo en la imagen para detectar clics
        self.rect = self.img_tower.get_rect(topleft=(x, y)) # (x, y) donde se va mostrar el cañon en la tienda
        self. price = price
        self.money = money # para acceder al dinero del jugador
    
    def draw(self, screen):
        screen.blit(self.img_tower, self.rect)
        screen.blit(pygame.font.Font(None, 24).render(f"${self.price}", True, (255, 255, 255)), (self.rect.x + 10, self.rect.y + self.rect.height - 20))

    def is_clicked(self, pos):
        # Si el jugador hizo clic sobre el cañon de la tienda, devuelve true
        return self.rect.collidepoint(pos) # pos es la posicion del mouse cuando se hace el clic