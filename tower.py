import pygame
import constantes as c
from bullet import Bullet

class Tower:

    def __init__(self, pos, scope, damage, att_speed, target, price, image):
        self.pos = pos
        self.scope = scope
        self.damage = damage
        self.att_speed = att_speed
        self.target = target
        self.price = price
        self.img = image
        self.enemies = False
        self.attack_timer = 0
        self.bullet_active = None
    
    def set_tower(self, x, y):
        self.pos = (x, y)
    
    def draw_scope(self, screen):
        pygame.draw.circle(screen, c.white, self.pos ,self.scope, 1)

    def enemies_in_range(self, pos_enemy):
        xe, ye = pos_enemy
        xt, yt = self.pos
        if (xt - self.scope) <= xe <= (xt + self.scope):
            if (yt - self.scope) <= ye <= (yt + self.scope):
                self.enemies = True
                return True
        return False

    def shoot(self, enemies):
        if self.bullet_active and self.bullet_active.alive():
            return None
        
        current_time = pygame.time.get_ticks()
        cooldown = self.att_speed  # milisegundos
        
        for enemy in enemies:
            if enemy.alive() and self.enemies_in_range(enemy.pos) and current_time - self.attack_timer >= cooldown:
                bullet = Bullet(pos=self.pos, target=enemy, speed=10, damage=self.damage, image_path="imgs/bullet.png")
                self.attack_timer = current_time 
                return bullet
            
            # ARREGLAR!!!
        return None


    



    