import pygame
import constantes as c
from bullet import Bullet
import math
from enemy import *
import sounds as s
from upgrade_button import UpBut 
#Primero creo la clase padre de las defensas, en este caso, Tower
class Tower(pygame.sprite.Sprite):
    def __init__(self, pos, scope, damage, base_att_speed, target, price, image, angle, game_speed, water, shoot_armored, sound):
        super().__init__()
        self.pos = pos
        self.scope = scope
        self.damage = damage
        self.game_speed = game_speed
        self.base_att_speed = base_att_speed
        self.att_speed = base_att_speed / game_speed
        self.target = target
        self.price = price
        self.original_img = image
        self.water = water
        self.sound = sound
        self.shoot_armored = shoot_armored
        self.img = self.original_img    #hasta aca son los atributos propios de la torre
        self.rect = self.img.get_rect(center=pos)
        self.enemies = False
        self.attack_timer = 0
        self.bullet_active = None
        self.level = 0
        button_x = self.rect.centerx
        button_y = self.rect.bottom + 10
        self.upgrade_button = UpBut(50, 100, c.UPGRADE_BUT_IMG, (button_x, button_y))
        self.showing_button = False
        self.max_level = 3
        self.costs = [250, 600, 800]
        self.selected = False
        self.angle = angle  #los ultimos son parametros usados en colisiones/animaciones
        self.rect = self.img.get_rect(center=self.pos)
        self.update_upgrade_button_pos()

    
    def set_tower(self, x, y):
        self.rect.center = (x, y)
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
                if (enemy.armored and self.shoot_armored) or not enemy.armored:
                    bullet = Bullet(pos=self.pos, target=enemy, speed=1000, damage=self.damage, image_path="imgs/bullet.png")
                    self.attack_timer = current_time
                    self.bullet_active = bullet
                    self.sound.play()
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

    def upgrade(self, money, mouse_celd): #mouse_celd llama a get_celd de la clase grilla, devuelve la celda donde esta el mouse
        #if self.selected:
            #self.upgrade_button.pos = (self.rect.centerx, self.rect.bottom + 10)
            #self.upgrade_button.rect = self.upgrade_button.img.get_rect(center=self.upgrade_button.pos)
            #self.upgrade_button.draw(screen, f'${self.costs[self.level]}')
        if money.cant_total >= self.costs[self.level] and self.level < self.max_level:
            money.cant_total -= self.costs[self.level]
            self.level += 1
            if mouse_celd in (3, 4, 5, 6):
                if self.level == 1:
                    self.base_att_speed = self.base_att_speed / 2
                    self.att_speed = self.base_att_speed / self.game_speed
                if self.level == 2:
                    self.damage = self.damage * 1.2
                if self.level == 3:
                    self.damage = self.damage * 2

    def update_upgrade_button_pos(self):
        button_x = self.rect.centerx
        button_y = self.rect.bottom + 10
        self.upgrade_button.pos = (button_x, button_y)
        self.upgrade_button.rect = self.upgrade_button.img.get_rect(center=self.upgrade_button.pos)


    def update_img(self, tower):
        if isinstance(tower, Cannon):
            if tower.level == 1:
                self.original_img = c.LVL1_CANON
                self.img = self.original_img
            if tower.level == 2:
                self.original_img = c.LVL2_CANON
                self.img = self.original_img
            if tower.level == 3:
                self.original_img = c.LVL3_CANON
                self.img = self.original_img
        elif isinstance(tower, Ship):
            if tower.level == 1:               
                self.original_img = c.LVL1_SHIP
                self.img = self.original_img
            if tower.level == 2:
                self.original_img = c.LVL2_SHIP
                self.img = self.original_img
            if tower.level == 3:
                self.original_img = c.LVL3_SHIP
                self.img = self.original_img
        elif isinstance(tower, Sniper):
            if tower.level == 1:               
                self.original_img = c.LVL1_SNIPER
                self.img = self.original_img
            if tower.level == 2:
                self.original_img = c.LVL2_SNIPER
                self.img = self.original_img
            if tower.level == 3:
                self.original_img = c.LVL3_SNIPER
                self.img = self.original_img
        elif isinstance(tower, Basic):
            if tower.level == 2:
                self.original_img = c.LVL2_MONKEY
                self.img = self.original_img
            if tower.level == 3:               
                self.original_img = c.LVL3_MONKEY
                self.img = self.original_img

class Cannon(Tower):    #defensa fuerte
    def __init__(self, pos, game_speed):
        scope = 120
        damage = 300
        price = 450
        base_att_speed = 1000
        att_speed = base_att_speed / game_speed
        target = None
        shoot_armored = True
        water = False
        sound = s.canon_sound
        image = pygame.image.load("imgs/tower.png").convert_alpha()
        angle = 0
        super().__init__(pos, scope, damage, base_att_speed, target, price, image, angle, game_speed, water, shoot_armored, sound) #aca puedo llamar a la clase padre con el scope y damage definido

class Sniper(Tower):    #mas rango, dano, menos cadencia
    def __init__(self, pos, game_speed):
        scope = 1000
        damage = 100
        price = 500
        base_att_speed = 500
        att_speed = base_att_speed / game_speed
        target = None
        water = False
        sound = s.sniper_sound
        shoot_armored = False
        self.image = pygame.image.load("imgs/shooter.png").convert_alpha()
        angle = 30
        super().__init__(pos, scope, damage, base_att_speed, target, price, self.image, angle, game_speed, water, shoot_armored, sound) #aca puedo llamar a la clase padre con el scope y damage definido

class Basic(Tower):  #normal
    def __init__(self, pos, game_speed):
        scope = 90
        damage = 100
        price = 200
        base_att_speed = 500
        att_speed = base_att_speed / game_speed
        target = None
        water = False
        shoot_armored = False
        angle = 0
        image = pygame.image.load("imgs/fast_monkey.png").convert_alpha()
        sound = s.monkey_sound
        super().__init__(pos, scope, damage, base_att_speed, target, price, image, angle, game_speed, water, shoot_armored,sound)

class Ship(Tower):  #en el agua
    def __init__(self, pos, game_speed):
        scope = 220
        damage = 150
        price = 450
        base_att_speed = 900
        att_speed = base_att_speed / game_speed
        target = None
        water = True
        shoot_armored = False
        angle = 0
        sound = s.canon_sound
        image = pygame.image.load("imgs/ship.png").convert_alpha()
        super().__init__(pos, scope, damage, base_att_speed, target, price, image, angle, game_speed, water, shoot_armored,sound)