import pygame
from money import Money
from sounds import *
class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos, base_speed, health, image, path, blinded, game_speed=1):
        super().__init__() #Hereda el init de la clase padre Sprite que viene con pygame
        self.pos = pos
        self.base_speed = base_speed
        self.speed = base_speed * game_speed
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
        if abs(new_x - xt) < 4 and abs(new_y - yt) < 4:
            if self.target_pos_index < len(self.path) - 1:
                self.target_pos_index += 1
        #que se hagan rojos
        if self.health <= 100 and not self.blinded:
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
            self.image = pygame.image.load("imgs/bloon_explotion.png")
            self.kill()
            money.add_money(5)
        if (self.pos[0] - self.path[-1][0] < 2) and (self.pos[1] - self.path[-1][1] < 2):
            self.kill()
            balloon_sound.play()
            if life.cant_total > int(self.health/100):
                life.lose_life(int(self.health/100)) # Asumiendo que la vida se pierde proporcionalmente a la salud del enemigo
            elif life.cant_total <= int(self.health/100):
                life.lose_life(life.cant_total)

    def draw(self, screen):

        rect = self.image.get_rect(center=(int(self.pos[0]), int(self.pos[1])))
        screen.blit(self.image, rect)

    def update_speed(self, game_speed):
        self.speed = self.base_speed * game_speed

class Red_Ballon(Enemy): 
    def __init__(self, game_speed):
        base_speed = 50
        speed = base_speed * game_speed
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
        super().__init__(pos, base_speed, health, image, path, blinded, game_speed)

class Blue_Ballon(Enemy):
    def __init__(self, game_speed):
        base_speed = 75
        speed = base_speed * game_speed
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
        super().__init__(pos, base_speed, health, image, path, blinded, game_speed)

class Green_Ballon(Enemy):
    def __init__(self, game_speed):
        base_speed = 90
        speed = base_speed * game_speed
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
    def __init__(self, game_speed):
        base_speed = 110
        speed = base_speed * game_speed
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
        super().__init__(pos, base_speed, health, image, path, blinded, game_speed)

class Pink_Ballon(Enemy):
    def __init__(self, game_speed):
        base_speed = 120
        speed = base_speed * game_speed
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
        super().__init__(pos, base_speed, health, image, path, blinded, game_speed)

class Blinded_Ballon(Enemy):
    def __init__(self, game_speed):
        base_speed = 50
        speed = base_speed * game_speed
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
        image = pygame.image.load("imgs/blinded_balloon.png").convert_alpha()
        super().__init__(pos, base_speed, health, image, path, blinded, game_speed)