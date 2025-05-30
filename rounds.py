import pygame

spawn_timer = pygame.time.get_ticks()
enemy_spawn_interval = 300  # milisegundos
enemy_count = 0
max_enemies = 30
class Round:
    
    def __init__(self, list_enemies):
        self.round = 0
        self.list_enemies = list_enemies
        self.is_active = False
        self.difficulty = 1

    def new_round(self):
        