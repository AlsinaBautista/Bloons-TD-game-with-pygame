import pygame
from enemy import Enemy

class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos, target, speed, damage, image_path):
        super().__init__()
        self.pos = pos
        self.target = target
        self.speed = speed
        self.damage = damage
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=self.pos)
        
    def update(self):
        x, y = self.pos
        xt, yt = self.target.pos
        direction = (xt - x, yt - y)
        magnitude = (direction[0]**2 + direction[1]**2)**0.5
        n_direction = (direction[0] / magnitude, direction[1] / magnitude)
        mov = (n_direction[0] * self.speed, n_direction[1] * self.speed)
        new_x = self.pos[0] + mov[0]
        new_y = self.pos[1] + mov[1]
        self.pos = (new_x, new_y)
        self.rect.center = (int(new_x), int(new_y))
        if ((new_x - xt) ** 2 + (new_y - yt) ** 2) ** 0.5 <= 10:
            self.target.health -= self.damage
            self.kill()




    
    

    