import pygame
import constantes as c
from map import Map
from bullet import Bullet
import sys
from money import Money
from life import Life
from shop import Shop 
from temporal_msg import TempMsg
from tower import *
from enemy import *
from grid import *

# Al principio del archivo
def excepthook(type, value, traceback):
    print("ERROR NO CAPTURADO:", type, value)
    pygame.quit()
    sys.exit()

sys.excepthook = excepthook

pygame.init()

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
icon = pygame.image.load("imgs/icono_globos.jpeg")
pygame.display.set_icon(icon)
pygame.display.set_caption("Bloons TD")

map = Map("imgs/fondo.png")
enemies = pygame.sprite.Group()
new_enemy = Enemy(c.ENEMY_POS, c.ENEMY_SPEED, c.ENEMY_HEALTH, c.ENEMY_IMG, c.ENEMY_PATH, False)
enemies.add(new_enemy)

# Imagen de torre dummy (puede ser reemplazada luego)

# Imagen de towers para shop
canon_img_shop = pygame.image.load("imgs/tower_shop.png").convert_alpha()
sniper_img_shop = pygame.image.load("imgs/shooter_shop.png").convert_alpha()
fast_mokey_img_shop = pygame.image.load("imgs/fast_mokey_shop.png").convert_alpha()

bullets = pygame.sprite.Group()

money_img = pygame.image.load("imgs/money.png")
money = Money(750, money_img)
life_img = pygame.image.load("imgs/life.png")
life = Life(20, life_img)

# Tienda y drag (torre en mouse)
shop_canon = Shop(canon_img_shop, 810, 10, 300, money)
shop_sniper = Shop(sniper_img_shop, 890, 10, 500, money)
shop_fast_monkey = Shop(fast_mokey_img_shop, 810, 110, 450, money)
dragging_tower = None # Variable que indica si el jugador esta arrastrando una torre desde la tienda
towers = pygame.sprite.Group() # Grupo que contiene todas las torres colocadas en el mapa

spawn_timer = pygame.time.get_ticks()
enemy_spawn_interval = 300  # milisegundos
enemy_count = 0
enemy_blue = 0
max_red = 30
max_blue = 30

active_msg = []
run = True
while run:
    delta_time = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            dragging_tower = shop_canon.shop_items(dragging_tower, Cannon, screen, towers, all_sprites, pos, active_msg)
            dragging_tower = shop_sniper.shop_items(dragging_tower, Sniper, screen, towers, all_sprites, pos, active_msg)
            dragging_tower = shop_fast_monkey.shop_items(dragging_tower, Fast, screen, towers, all_sprites, pos, active_msg)

    map.draw_background(screen)
    #map.draw_celds(screen, c.white, c.CELD)

    current_time = pygame.time.get_ticks()

    if enemy_count < max_red and current_time - spawn_timer >= enemy_spawn_interval:
        new_enemy = Red_Ballon()
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)
        enemy_count += 1
        spawn_timer = current_time 

    if enemy_blue < max_blue and current_time - spawn_timer >= enemy_spawn_interval:
        new_enemy = Blue_Ballon()
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)
        enemy_blue += 1
        spawn_timer = current_time 
    
    for enemy in enemies:
        enemy.update(money,life)
        enemy.draw(screen)

    # Torres colocadas desde la tienda
    for tower in towers:
        bullet = tower.shoot(enemies)
        if bullet:
            bullets.add(bullet)
            all_sprites.add(bullet)

    bullets.update(delta_time)
    bullets.draw(screen)

    money.draw(screen)
    life.draw(screen)

    # Dibujo de la tienda
    inventory_height = c.HEIGHT
    inventory_rect = pygame.Rect(c.WIDTH - c.INVENTORY_WIDTH, 0, c.INVENTORY_WIDTH, inventory_height)
    pygame.draw.rect(screen, (191,158,83), inventory_rect) # Dibuja el fondo de la tienda
    shop_canon.draw(screen) # Dibuja la torre disponible en la tienda 
    shop_sniper.draw(screen)
    shop_fast_monkey.draw(screen)

    # Dibujo de las torres colocadas
    for tower in towers:
        screen.blit(tower.img, (tower.pos[0] - tower.img.get_width()//2, tower.pos[1] - tower.img.get_height()//2))
        #tower.draw_scope(screen)
    
    # Dar el efecto de que el mouse lleva al item del cañon
    if dragging_tower is not None:
        mouse_pos = pygame.mouse.get_pos() # Posicion actual del mouse
        # Dibuja alcance
        scope_surface = dragging_tower.draw_scope(screen)
        screen.blit(scope_surface, (mouse_pos[0] - dragging_tower.scope, mouse_pos[1] - dragging_tower.scope))
        dragging_tower.set_tower(*mouse_pos) # Actualiza la posicion de la torre arrastrada
        screen.blit(dragging_tower.img, (mouse_pos[0] - dragging_tower.img.get_width()//2, mouse_pos[1] - dragging_tower.img.get_height()//2)) # Dibuja la imagen de la torre en la pantalla, de forma que su centro este exactamente donde esta el mouse

    if life.cant_total <= 0:
        font = pygame.font.Font('fonts/OETZTYP_.TTF', 48)
        text = font.render("GAME OVER", True, c.RED)
        text_rect = text.get_rect(center=(c.WIDTH // 2, c.HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        run = False
    
    for m in active_msg[:]:
        if m.visible:
            m.show_msg(screen)
        else:
            active_msg.remove(m)

        
    #clock.tick(60)


    pygame.display.update()

pygame.quit()
