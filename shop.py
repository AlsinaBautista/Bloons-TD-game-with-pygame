import pygame
from money import *

class Shop(pygame.sprite.Sprite):
    def __init__(self, img_tower, x, y, price, money):
        self.img_tower = img_tower
        self.rect = self.img_tower.get_rect(topleft=(x, y)) # Detect clicks
        self. price = price
        self.money = money
    
    def draw(self, screen):
        screen.blit(self.img_tower, self.rect)

    def get_money(self):
        return self.money.get_money()


    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)