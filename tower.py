import pygame
import constantes as c
from bullet import Bullet
import math
from enemy import *
#Primero creo la clase padre de las defensas, en este caso, Tower
class Tower(pygame.sprite.Sprite):
    def __init__(self, pos, scope, damage, base_att_speed, target, price, image, angle, game_speed):
        super().__init__()
        self.pos = pos
        self.scope = scope
        self.damage = damage
        self.base_att_speed = base_att_speed
        self.att_speed = base_att_speed / game_speed
        self.target = target
        self.price = price
        self.original_img = image
        self.img = self.original_img    #hasta aca son los atributos propios de la torre
        self.enemies = False
        self.attack_timer = 0
        self.bullet_active = None
        self.rect = self.img.get_rect(center=pos)
        self.angle = angle  #los ultimos son parametros usados en colisiones/animaciones
    
    def set_tower(self, x, y):
        self.pos = (x, y)   #cambia la posicion a la que se le pasa

    def draw_scope(self):
        """Devuelve una superficie con el alcance (scope) dibujado como un círculo transparente."""
        diameter = self.scope * 2
        surface = pygame.Surface((diameter, diameter), pygame.SRCALPHA)  # Soporta transparencia
        pygame.draw.circle(surface, (230, 230, 230, 100), (self.scope, self.scope), self.scope)
        return surface

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
                bullet = Bullet(pos=self.pos, target=enemy, speed=1000, damage=self.damage, image_path="imgs/bullet.png")
                self.attack_timer = current_time
                self.bullet_active = bullet
                return bullet
        return None
    
    def rotate(self, enemy_pos):

        x = enemy_pos[0] - self.pos[0]
        y = enemy_pos[1] - self.pos[1]
        angle_rad = math.atan2(-y, x)
        self.angle = math.degrees(angle_rad)
        self.img = pygame.transform.rotate(self.original_img, self.angle + 90)
        self.rect = self.img.get_rect(center=self.pos)

    def update_att_speed(self, game_speed):
        self.att_speed = self.base_att_speed / game_speed

class Basic(Tower):
    def __init__(self, pos, game_speed):
        scope = 100
        damage = 100
        price = 300
        base_att_speed = 500
        att_speed = base_att_speed / game_speed
        target = None
        image = pygame.image.load("imgs/tower.png").convert_alpha()
        angle = 0
        super().__init__(pos, scope, damage, base_att_speed, target, price, image, angle, game_speed)

class Cannon(Tower):    #defensa fuerte
    def __init__(self, pos, game_speed):
        scope = 100
        damage = 100
        price = 300
        base_att_speed = 500
        att_speed = base_att_speed / game_speed
        target = None
        image = pygame.image.load("imgs/tower.png").convert_alpha()
        angle = 0
        super().__init__(pos, scope, damage, base_att_speed, target, price, image, angle, game_speed) #aca puedo llamar a la clase padre con el scope y damage definido

class Sniper(Tower):    #mas rango, dano, menos cadencia
    def __init__(self, pos, game_speed):
        scope = 1000
        damage = 500
        price = 500
        base_att_speed = 1000
        att_speed = base_att_speed / game_speed
        target = None
        image = pygame.image.load("imgs/shooter.png").convert_alpha()
        angle = 30
        super().__init__(pos, scope, damage, base_att_speed, target, price, image, angle, game_speed) #aca puedo llamar a la clase padre con el scope y damage definido


class Fast(Tower):  #mas cadencia
    def __init__(self, pos, game_speed):
        scope = 200
        damage = 100
        price = 450
        base_att_speed = 300
        att_speed = base_att_speed / game_speed
        target = None
        angle = 0
        image = pygame.image.load("imgs/fast_monkey.png").convert_alpha()
        super().__init__(pos, scope, damage, base_att_speed, target, price, image, angle, game_speed)

class Ship(Tower):  #mas cadencia
    def __init__(self, pos, game_speed):
        scope = 200
        damage = 100
        price = 450
        base_att_speed = 1000
        att_speed = base_att_speed / game_speed
        target = None
        image = pygame.image.load("imgs/ship.png").convert_alpha()
        super().__init__(pos, scope, damage, base_att_speed, target, price, image, game_speed)