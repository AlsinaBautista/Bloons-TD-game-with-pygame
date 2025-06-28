import pygame
from enemy import *
import math

class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos, target, speed, damage, image_path):
        super().__init__()
        self.pos = pos
        self.target = target
        self.base_speed = speed
        self.speed = speed
        self.damage = damage
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.pos)
        
    def update(self, delta_time):
        """
        Update the bullet's position towards the target and check for collision.
        Calculates the direction towards the target, moves the bullet
        in that direction, and checks if it has reached the target to apply damage.
        -------------------------------------------------------------------------
        Arguments:
            delta_time (float): the time since the last update in seconds.
        """
        self.rotate(self.target.pos)
        x, y = self.pos
        xt, yt = self.target.pos
        direction = (xt - x, yt - y)
        magnitude = (direction[0]**2 + direction[1]**2)**0.5
        n_direction = (direction[0] / magnitude, direction[1] / magnitude)
        mov = (n_direction[0] * self.speed * delta_time, n_direction[1] * self.speed * delta_time)
        new_x = self.pos[0] + mov[0]
        new_y = self.pos[1] + mov[1]
        self.pos = (new_x, new_y)
        self.rect.center = (int(new_x), int(new_y))
        if ((new_x - xt) ** 2 + (new_y - yt) ** 2) ** 0.5 <= 10:
            self.target.health -= self.damage
            self.kill()
            
    def rotate(self, enemy_pos):
        '''
        Rotate the bullet image to face the enemy position.
        -------------------------------------------------------------------------
        Arguments:
            enemy_pos (tuple): The (x, y) position of the enemy to face.
        '''
        x = enemy_pos[0] - self.pos[0]
        y = enemy_pos[1] - self.pos[1]
        angle_rad = math.atan2(-y, x)
        self.angle = math.degrees(angle_rad)
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.pos)