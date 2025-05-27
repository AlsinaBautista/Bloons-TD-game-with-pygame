import pygame
from money import Money

class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos, speed, health, image, path, blinded):
        super().__init__() #Hereda el init de la clase padre Sprite que viene con pygame
        self.pos = pos
        self.speed = speed
        self.health = health
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.path = path
        self.target_pos_index = 1
        self.blinded = blinded
        self.last_update_time = pygame.time.get_ticks()


    def set_pos(self, x, y):
        n_pos = (x, y)
        self.pos = n_pos
    
    def update(self, money, life):
        current_time = pygame.time.get_ticks()
        delta_time = (current_time - self.last_update_time) / 1000.0  # en segundos
        self.last_update_time = current_time
        direction = (self.path[self.target_pos_index][0] - self.pos[0], self.path[self.target_pos_index][1] - self.pos[1])
        x, y = direction
        magnitude = (x**2 + y**2)**0.5
        n_direction = (x / magnitude, y / magnitude)
        mov = (n_direction[0] * self.speed * delta_time, n_direction[1] * self.speed * delta_time)
        new_x = self.pos[0] + mov[0]
        new_y = self.pos[1] + mov[1]
        self.set_pos(new_x, new_y)
        self.rect.center = (int(new_x), int(new_y))
        xt, yt = self.path[self.target_pos_index]
        if abs(new_x - xt) < 2 and abs(new_y - yt) < 2:
            if self.target_pos_index < len(self.path) - 1:
                self.target_pos_index += 1
        #que se hagan rojos
        if self.health <= 100:
            self.image = pygame.image.load('imgs/bloon.png')
        
        #que se hagan azules
        if 100 < self.health <= 200:
            self.image = pygame.image.load('imgs/blue_balloon.png')
        
        #que se hagan verdes
        if 200 < self.health <= 300:
            self.image = pygame.image.load('imgs/green_balloon.png')

        #que se hagan coloridos
        if 300 < self.health <= 400:
            self.image = pygame.image.load('imgs/colored_balloon.png')
        
        #que se hagan rosas
        if 400 < self.health <= 500:
            self.image = pygame.image.load('imgs/pink_balloon.png')

        if self.health <= 0:
            self.kill()
            money.add_money(25)
        if self.pos[0] == 501 and self.pos[1] <5:
            self.kill()
            life.lose_life(self.health)
            

    def draw(self, screen):

        rect = self.image.get_rect(center=(int(self.pos[0]), int(self.pos[1])))
        screen.blit(self.image, rect)

class Red_Ballon(Enemy): 
    def __init__(self):
        speed = 100
        health = 100
        pos = (0, 265)
        path = [
                (0, 265),   # Inicio fuera de pantalla (izquierda)
                (29, 265),     
                (265, 265),
                (265, 147),
                (383, 147),
                (383, 383),
                (265, 383),
                (265, 501),
                (619, 501),
                (619, 442),
                (678, 442),
                (678, 383),
                (737, 383),
                (737, 206),
                (560, 206),
                (560,  88),
                (501,  88),
                (501,  0)
                            ]
        blinded = False
        image = pygame.image.load("imgs/bloon.png")
        super().__init__(pos, speed, health, image, path, blinded)

class Blue_Ballon(Enemy):
    def __init__(self):
        speed = 125
        health = 200
        pos = (0, 265)
        blinded = False
        path = [
                (0, 265),   # Inicio fuera de pantalla (izquierda)
                (29, 265),     
                (265, 265),
                (265, 147),
                (383, 147),
                (383, 383),
                (265, 383),
                (265, 501),
                (619, 501),
                (619, 442),
                (678, 442),
                (678, 383),
                (737, 383),
                (737, 206),
                (560, 206),
                (560,  88),
                (501,  88),
                (501,  0)
                            ]
        image = pygame.image.load("imgs/blue_balloon.png")
        super().__init__(pos, speed, health, image, path, blinded)


class Green_Ballon(Enemy):
    def __init__(self):
        speed = 150
        health = 300
        pos = (0, 265)
        blinded = False
        path = [
                (0, 265),   # Inicio fuera de pantalla (izquierda)
                (29, 265),     
                (265, 265),
                (265, 147),
                (383, 147),
                (383, 383),
                (265, 383),
                (265, 501),
                (619, 501),
                (619, 442),
                (678, 442),
                (678, 383),
                (737, 383),
                (737, 206),
                (560, 206),
                (560,  88),
                (501,  88),
                (501,  0)
                            ]
        image = pygame.image.load("imgs/green_balloon.png")
        super().__init__(pos, speed, health, image, path, blinded)

class Colored_Ballon(Enemy):
    def __init__(self):
        speed = 175
        health = 400
        pos = (0, 265)
        blinded = False
        path = [
                (0, 265),   # Inicio fuera de pantalla (izquierda)
                (29, 265),     
                (265, 265),
                (265, 147),
                (383, 147),
                (383, 383),
                (265, 383),
                (265, 501),
                (619, 501),
                (619, 442),
                (678, 442),
                (678, 383),
                (737, 383),
                (737, 206),
                (560, 206),
                (560,  88),
                (501,  88),
                (501,  0)
                            ]
        image = pygame.image.load("imgs/colored_balloon.png")
        super().__init__(pos, speed, health, image, path, blinded)

class Pink_Ballon(Enemy):
    def __init__(self):
        speed = 200
        health = 500
        pos = (0, 265)
        blinded = False
        path = [
                (0, 265),   # Inicio fuera de pantalla (izquierda)
                (29, 265),     
                (265, 265),
                (265, 147),
                (383, 147),
                (383, 383),
                (265, 383),
                (265, 501),
                (619, 501),
                (619, 442),
                (678, 442),
                (678, 383),
                (737, 383),
                (737, 206),
                (560, 206),
                (560,  88),
                (501,  88),
                (501,  0)
                            ]
        image = pygame.image.load("imgs/pink_balloon.png")
        super().__init__(pos, speed, health, image, path, blinded)

class Blinded_Ballon(Enemy):
    def __init__(self):
        speed = 200
        health = 8
        pos = (0, 265)
        blinded = True
        path = [
                (0, 265),   # Inicio fuera de pantalla (izquierda)
                (29, 265),     
                (265, 265),
                (265, 147),
                (383, 147),
                (383, 383),
                (265, 383),
                (265, 501),
                (619, 501),
                (619, 442),
                (678, 442),
                (678, 383),
                (737, 383),
                (737, 206),
                (560, 206),
                (560,  88),
                (501,  88),
                (501,  0)
                            ]
        image = pygame.image.load("imgs/pink_balloon.png")
        super().__init__(pos, speed, health, image, path, blinded)