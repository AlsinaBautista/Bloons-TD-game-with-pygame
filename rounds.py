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
        self.reward = [50, 50, 75, 75,
            100, 100, 120, 120, 140,           # nivel 1–5
            140, 160, 160, 180, 180,           # nivel 6–10
            200, 200, 220, 220, 240,           # nivel 11–15
            260, 260, 280, 280, 300,           # 16–20
            320, 320, 340, 360, 380,           # 21–25
            400, 420, 440, 460, 480,           # 26–30
            500, 520, 540, 560, 580,           # 31–35
            600, 630, 660, 690, 720,           # 36–40
            750, 780, 820, 870, 930, 1000      # 41–50
            ]        
        self.reward_given = True

    def new_round(self, current_time, money):
        if self.round < len(self.list_rounds): 
            self.reward_given = False
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
            elif enemy_type == "armored":
                new_enemy = Armored_Ballon(game_speed)

            if new_enemy:
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            self.spawn_timer = current_time

        if not self.pending_enemies and not self.all_enemies_spawned:
            self.all_enemies_spawned = True 

    def is_round_over(self, enemies_group, money):
        if self.all_enemies_spawned and not enemies_group.sprites():
            self.is_active = False
            return True

    def draw_text(self, screen):
        text = self.font.render(f"Round {self.round}/50", True, (255, 255, 255)) 
        text_rect = text.get_rect(center=(675, 30))
        screen.blit(text, text_rect)
