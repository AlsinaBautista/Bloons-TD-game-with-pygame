import pygame

RED = (245,48,18)
GREY = (0, 0, 0, 40)
TRANS = (0, 0, 0, 100)
WHITE = (255, 255, 255)
BROWN = (136,86,0)
TRANS_GREEN = (23, 134, 21, 80)
TRANS_RED = (245, 48, 18, 80)
WIDTH = 992
HEIGHT = 532
CELD = 59
INVENTORY_WIDTH = 225
GRID_WIDTH = (WIDTH - INVENTORY_WIDTH) // CELD
GRID_HEIGHT = HEIGHT // CELD
ENEMY_PATH = [
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

ENEMY_HEALTH = 1
ENEMY_IMG = pygame.image.load("imgs/bloon.png")
ENEMY_SPEED = 100
ENEMY_POS = (0, 265)

OCCUPIED_CELLS = [
    [(0, 0), 1], [(1, 0), 1], [(2, 0), 1], [(10, 0), 1],  [(11, 0), 1], [(12, 0), 1], [(13, 0), 1],
    [(0, 1), 1], [(12, 1), 1], [(13, 1), 1],
    [(0, 2), 1],[(13, 2), 1],
    [(13, 3), 1], 
    [(9, 4), 2], [(10, 4), 2],[(11, 4), 1],[(13, 4), 1], 
    [(9, 5), 2], [(10, 5), 2],[(11, 5), 1],[(13, 5), 1],
    [(0, 6), 1], [(8, 6), 1], [(9, 6), 2], [(10, 6), 2],[(13, 6), 1], 
    [(0, 7), 1], [(1, 7), 1],[(12, 7), 1], [(13, 7), 1], 
    [(0, 8), 1], [(1, 8), 1], [(2, 8), 1],[(11, 8), 1], [(12, 8), 1], [(13, 8), 1]
    
]

SPEED_BUTTON_IMG = pygame.image.load("imgs/speed_button.png")
ROUND_BUT_IMG = pygame.image.load("imgs/next_round_button.png")
MUTE_BUT_IMG = pygame.image.load("imgs/mute_but.png")
UNMUTE_BUT_IMG = pygame.image.load("imgs/unmute_but.png")
UPGRADE_BUT_IMG = pygame.image.load("imgs/rect_text.png")
LVL1_CANON = pygame.image.load("imgs/lvl1_canon.png")
LVL2_CANON = pygame.image.load("imgs/lvl2_canon.png")
LVL3_CANON = pygame.image.load("imgs/lvl3_canon.png")
LVL1_SHIP = pygame.image.load("imgs/ship_lvl1.png")
LVL2_SHIP = pygame.image.load("imgs/ship_lvl2.png")
LVL3_SHIP = pygame.image.load("imgs/ship_lvl3.png")
LVL1_SNIPER = pygame.image.load("imgs/sniper_lvl1.png")
LVL2_SNIPER = pygame.image.load("imgs/sniper_lvl2.png")
LVL3_SNIPER = pygame.image.load("imgs/sniper_lvl3.png")
LVL1_MONKEY = pygame.image.load("imgs/fast_monkey_lvl1.png")
LVL2_MONKEY = pygame.image.load("imgs/fast_monkey_lvl2.png")
LVL3_MONKEY = pygame.image.load("imgs/fast_monkey_lvl3.png")

VICTORY_IMG = pygame.image.load("imgs/victory.png")
DEFEAT_IMG = pygame.image.load("imgs/defeat.png")