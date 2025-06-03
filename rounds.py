import pygame
import list_rounds as lr
from enemy import *

class Round:
    
    def __init__(self, list_rounds):
        self.round = 0
        self.list_rounds = list_rounds
        """self.enemy_type = list_enemies[0]
        self.enemy_cant = list_enemies[1]
        self.spawn_interval = list_enemies[2]"""
        self.is_active = False
        self.spawn_timer = pygame.time.get_ticks()
        self.spawn_interval = 0
        self.pending_enemies = []

    def new_round(self, current_time):
        self.pending_enemies = []
        round = self.list_rounds[self.round]
        self.spawn_interval = round["interval"]/2
        for enemy in round["enemies"]:
            enemy_class = enemy["type"]
            cant = enemy["cant"]
            self.pending_enemies.extend([enemy_class.lower()] * cant)
            self.spawn_timer = current_time
        self.is_active = True

    def update(self, current_time, game_speed, enemies, all_sprites):
         
        if current_time - self.spawn_timer >= self.spawn_interval and self.pending_enemies:
            enemy = self.pending_enemies.pop(0)
            if enemy == "red":
                new_enemy = Red_Ballon(game_speed)
            elif enemy == "blue":
                new_enemy = Blue_Ballon(game_speed)
            elif enemy == "green":
                new_enemy = Green_Ballon(game_speed)
            elif enemy == "pink":
                new_enemy = Pink_Ballon(game_speed)
            elif enemy == "colored":
                new_enemy = Colored_Ballon(game_speed)
            elif enemy == "blinded":
                new_enemy = Blinded_Ballon(game_speed)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
            self.spawn_timer = current_time
        
        if len(self.pending_enemies) == 0:
            self.is_active = False
            self.round += 1