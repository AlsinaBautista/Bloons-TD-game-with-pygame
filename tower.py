import pygame
import constantes as c

class Tower:

    def __init__(self, pos, scope, damage, att_speed, target, price, image):
        self.pos = pos
        self.scope = scope
        self.damage = damage
        self.att_speed = att_speed
        self.target = target
        self.price = price
        self.img = image
    
    def set_tower(self, x, y):
        self.pos = (x, y)
    
    def draw_scope(self, screen):
        pygame.draw.circle(screen, c.white, self.pos ,self.scope, 1)

    def enemies_in_range(self, pos_enemy):
        xe, ye = pos_enemy
        xt, yt = self.pos
        if (xt - self.scope) <= xe <= (xt + self.scope):
            if (yt - self.scope) <= ye <= (yt + self.scope):
                return True
        return False
    



    