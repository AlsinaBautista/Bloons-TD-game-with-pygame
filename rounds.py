import pygame

spawn_timer = pygame.time.get_ticks()
enemy_spawn_interval = 300  # milisegundos
enemy_count = 0
max_enemies = 30
class Round:
    def __init__(self, cant_enemies):
        self.round = 0
        self.cant_enemies = cant_enemies

    def ballon_types()