import pygame
import constantes as c
from bullet import Bullet
import math

class Tower(pygame.sprite.Sprite):

    def __init__(self, pos, scope, damage, att_speed, target, price, image):
        super().__init__()
        self.pos = pos
        self.scope = scope
        self.damage = damage
        self.att_speed = att_speed
        self.target = target
        self.price = price
        self.original_img = image
        self.img = self.original_img
        self.enemies = False
        self.attack_timer = 0
        self.bullet_active = None
        self.rect = self.img.get_rect(center=pos)
        self.angle = 0
    
    def set_tower(self, x, y):
        self.pos = (x, y)
    
    def draw_scope(self, screen):
        pygame.draw.circle(screen, c.white, self.pos ,self.scope, 1)

    def enemies_in_range(self, pos_enemy):
        xe, ye = pos_enemy
        xt, yt = self.pos
        dist = ((xe - xt) ** 2 + (ye - yt) ** 2) ** 0.5
        if dist <= self.scope:
            return True
        return False

    def shoot(self, enemies):
        if self.bullet_active and self.bullet_active.alive():
            return None
        
        current_time = pygame.time.get_ticks()
        cooldown = self.att_speed  # milisegundos
        
        for enemy in enemies:
            if enemy.alive() and self.enemies_in_range(enemy.pos) and current_time - self.attack_timer >= cooldown:
                self.rotate(enemy.pos)
                bullet = Bullet(pos=self.pos, target=enemy, speed=500, damage=self.damage, image_path="imgs/bullet.png")
                self.attack_timer = current_time
                self.bullet_active = bullet 
                return bullet
        return None
    
    def rotate(self, enemy_pos):

        x = enemy_pos[0] - self.pos[0]
        y = enemy_pos[1] - self.pos[1]
        angle_rad = math.atan2(-y, x)
        self.angle = math.degrees(angle_rad)
        self.img = pygame.transform.rotate(self.original_img, self.angle)
        self.rect = self.img.get_rect(center=self.pos)

class Cannon(Tower):
    def __init__(self, pos):
        scope = 200
        damage = 1
        price = 300
        att_speed = 500
        target = None
        image = pygame.image.load("imgs/tower.png").convert_alpha()
        super().__init__(pos, scope, damage, att_speed, target, price, image) #aca puedo llamar a la clase padre con el scope y damage definido

class Sniper(Tower):
    def __init__(self, pos):
        scope = 400
        damage = 5
        price = 600
        att_speed = 200
        target = None
        image = pygame.image.load("imgs/tower.png").convert_alpha()
        super().__init__(pos, scope, damage, att_speed, target, price, image) #aca puedo llamar a la clase padre con el scope y damage definido

class Strong(Tower):
    def __init__(self, pos):
        scope = 100
        damage = 10
        price = 1000
        att_speed = 200
        target = None
        image = pygame.image.load("imgs/tower.png").convert_alpha()
        super().__init__(pos, scope, damage, att_speed, target, price, image)