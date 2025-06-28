import pygame
pygame.mixer.init()
# Archivos con sonido
# Se inicializa el mixer de pygame para poder reproducir sonidos
music = pygame.mixer.music.load('sounds/bloons_music.mp3')
game_over = pygame.mixer.Sound("sounds/game_over.mp3")
monkey_sound = pygame.mixer.Sound("sounds/monkey_shot.mp3")
balloon_sound = pygame.mixer.Sound("sounds/balloon_sound.mp3")
canon_sound = pygame.mixer.Sound('sounds/canon_sound.mp3')
sniper_sound = pygame.mixer.Sound('sounds/sniper_sound.mp3')
victory_sound = pygame.mixer.Sound("sounds/victory.mp3")