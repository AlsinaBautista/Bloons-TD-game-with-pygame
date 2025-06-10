import pygame
import list_rounds as lr
from enemy import *
import constantes as c

class Round:

    def __init__(self, list_rounds):
        self.round = 0
        self.list_rounds = list_rounds
        self.is_active = False
        self.spawn_timer = pygame.time.get_ticks()
        self.spawn_interval = 0
        self.pending_enemies = []
        self.font = pygame.font.Font("fonts/OETZTYP_.TTF", 24)
        self.all_enemies_spawned = False 

    def new_round(self, current_time):
        if self.round < len(self.list_rounds): 
            self.pending_enemies = []
            round_data = self.list_rounds[self.round] 
            self.spawn_interval = round_data["interval"]/2
            for enemy in round_data["enemies"]:
                enemy_class = enemy["type"]
                cant = enemy["cant"]
                self.pending_enemies.extend([enemy_class.lower()] * cant)
                self.spawn_timer = current_time
            self.is_active = True
            self.all_enemies_spawned = False 
            self.round += 1

    def update(self, current_time, game_speed, enemies, all_sprites):

        if self.pending_enemies and current_time - self.spawn_timer >= self.spawn_interval:
            enemy_type = self.pending_enemies.pop(0)
            new_enemy = None
            if enemy_type == "red":
                new_enemy = Red_Ballon(game_speed)
            elif enemy_type == "blue":
                new_enemy = Blue_Ballon(game_speed)
            elif enemy_type == "green":
                new_enemy = Green_Ballon(game_speed)
            elif enemy_type == "pink":
                new_enemy = Pink_Ballon(game_speed)
            elif enemy_type == "yellow":
                new_enemy = Yellow_Ballon(game_speed)
            elif enemy_type == "blinded":
                new_enemy = Blinded_Ballon(game_speed)

            if new_enemy:
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            self.spawn_timer = current_time

        if not self.pending_enemies and not self.all_enemies_spawned:
            self.all_enemies_spawned = True 

    def is_round_over(self, enemies_group):
        if self.all_enemies_spawned and not enemies_group.sprites():
            self.is_active = False
            return True

    def draw_text(self, screen):
        text = self.font.render(f"Ronda {self.round}/50", True, (255, 255, 255)) 
        text_rect = text.get_rect(center=(675, 30))
        screen.blit(text, text_rect)