import pygame
pygame.mixer.init()
music = pygame.mixer.music.load('fonts/bloons_music.mp3')
game_over = pygame.mixer.Sound("fonts/game_over.mp3")
shot_sound = pygame.mixer.Sound("fonts/shot.mp3")