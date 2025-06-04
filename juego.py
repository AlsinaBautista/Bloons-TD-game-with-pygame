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
from x2_button import *
from rounds import Round
import list_rounds as lr

# Al principio del archivo
#def excepthook(type, value, traceback):
#    print("ERROR NO CAPTURADO:", type, value)
#    pygame.quit()
#    sys.exit()
#
#sys.excepthook = excepthook

pygame.init() #inicializamos todos los modulos de pygame
pygame.mixer.init()
pygame.mixer.music.load('fonts/bloons_music.mp3')
pygame.mixer.music.play(-1) #para loop
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

# Imagen de towers para shop
canon_img_shop = pygame.image.load("imgs/tower_shop.png").convert_alpha()
sniper_img_shop = pygame.image.load("imgs/shooter_shop.png").convert_alpha()
ship_img_shop = pygame.image.load("imgs/ship_shop.png").convert_alpha()
fast_mokey_img_shop = pygame.image.load("imgs/fast_monkey_shop.png").convert_alpha()

bullets = pygame.sprite.Group()

money_img = pygame.image.load("imgs/money.png")
money = Money(750, money_img)
life_img = pygame.image.load("imgs/life.png")
life = Life(20, life_img)

# Tienda y drag (torre en mouse)
shop_canon = Shop(canon_img_shop, 790, 10, 300, money)
shop_sniper = Shop(sniper_img_shop, 895, 10, 500, money)
shop_fast_monkey = Shop(fast_mokey_img_shop, 790, 130, 450, money)
shop_ship = Shop(ship_img_shop, 895, 130, 450, money)
dragging_tower = None # Variable que indica si el jugador esta arrastrando una torre desde la tienda
towers = pygame.sprite.Group() # Grupo que contiene todas las torres colocadas en el mapa

# Imagen tacho de basura
trash_img = pygame.image.load("imgs/trash.png").convert_alpha()
trash_hover = pygame.image.load("imgs/trash_hover.png").convert_alpha()

spawn_timer = pygame.time.get_ticks()
"""enemy_spawn_interval = 300  # milisegundos
enemy_count = 0
enemy_blue = 0
max_red = 30
max_blue = 30"""

active_msg = []

game_speed = 1
speed_button = Button(c.SPEED_BUTTON, (c.WIDTH - c.INVENTORY_WIDTH - 50, c.HEIGHT - 50), 30)

grid = start_grid()

rounds_list = lr.rounds_list
round_manager = Round(rounds_list)

run = True
while run:
    delta_time = clock.tick(60) / 1000
    for event in pygame.event.get(): #el .event.get devuelve todos los eventos (teclado, mouse, etc.)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if speed_button.is_clicked(event.pos) and not dragging_tower:
                game_speed = speed_button.change_speed()
                # Aplicar nueva velocidad a enemigos
                for enemy in enemies:
                    enemy.update_speed(game_speed)

                # A proyectiles existentes
                for bullet in bullets:
                    bullet.speed = bullet.base_speed * game_speed

                if game_speed == 1:
                    enemy_spawn_interval = 300
                else:
                    enemy_spawn_interval = 150
                # A torres
                for tower in towers:
                    tower.att_speed = tower.base_att_speed / game_speed  # menor cooldown = más rápido
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            dragging_tower = shop_canon.shop_items(dragging_tower, Cannon, screen, towers, all_sprites, pos, active_msg, game_speed, grid)
            dragging_tower = shop_sniper.shop_items(dragging_tower, Sniper, screen, towers, all_sprites, pos, active_msg, game_speed, grid)
            dragging_tower = shop_fast_monkey.shop_items(dragging_tower, Fast, screen, towers, all_sprites, pos, active_msg, game_speed, grid)
            dragging_tower = shop_ship.shop_items(dragging_tower, Ship, screen, towers, all_sprites, pos, active_msg, game_speed, grid)
        
    map.draw_background(screen)
    #map.draw_celds(screen, c.white, c.CELD)

    current_time = pygame.time.get_ticks()

    if not round_manager.is_active and round_manager.round < len(rounds_list):
        round_manager.new_round(current_time)
    
    round_manager.update(current_time, game_speed, enemies, all_sprites)
    
    """if enemy_count < max_red and current_time - spawn_timer >= enemy_spawn_interval:
        new_enemy = Red_Ballon(game_speed)
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)
        enemy_count += 1
        spawn_timer = current_time 

    if enemy_blue < max_blue and current_time - spawn_timer >= enemy_spawn_interval:
        new_enemy = Blue_Ballon(game_speed)
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)
        enemy_blue += 1
        spawn_timer = current_time """
    
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

    speed_button.draw(screen)

    # Dibujo de las torres colocadas
    for tower in towers:
        screen.blit(tower.img, (tower.pos[0] - tower.img.get_width()//2, tower.pos[1] - tower.img.get_height()//2))
        grid.update_grid(tower)
        #tower.draw_scope(screen)
    
    # Dibujo de la tienda
    inventory_height = c.HEIGHT
    inventory_rect = pygame.Rect(c.WIDTH - c.INVENTORY_WIDTH, 0, c.INVENTORY_WIDTH, inventory_height)
    pygame.draw.rect(screen, (191,158,83), inventory_rect) # Dibuja el fondo de la tienda
    shop_canon.draw(screen) # Dibuja la torre disponible en la tienda 
    shop_sniper.draw(screen)
    shop_fast_monkey.draw(screen)
    shop_ship.draw(screen)
    # Dar el efecto de que el mouse lleva al item del cañon
    if dragging_tower is not None:
        # Muestra el tacho de basura
        trash_rect = Shop.draw_trash(screen, trash_img, trash_hover, mouse_pos)
        # Dibuja alcance
        if mouse_pos[0] <= c.WIDTH - c.INVENTORY_WIDTH:
            scope_surface = dragging_tower.draw_scope()
            screen.blit(scope_surface, (mouse_pos[0] - dragging_tower.scope, mouse_pos[1] - dragging_tower.scope))
        dragging_tower.set_tower(*mouse_pos) # Actualiza la posicion de la torre arrastrada
        #map.draw_celds_border(screen, c.WHITE, c.CELD)
        map.draw_celds(screen, grid, dragging_tower)
        screen.blit(dragging_tower.img, (mouse_pos[0] - dragging_tower.img.get_width()//2, mouse_pos[1] - dragging_tower.img.get_height()//2)) # Dibuja la imagen de la torre en la pantalla, de forma que su centro este exactamente donde esta el mouse

        # Deja de seleccionar el item de la tienda cuando toca el tacho de basura
        if event.type == pygame.MOUSEBUTTONDOWN:
            if trash_rect.collidepoint(mouse_pos):
                dragging_tower = None

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
    mouse_pos = pygame.mouse.get_pos() # Posicion actual del mouse
    speed_button.hover(screen, mouse_pos)

    pygame.display.update()

pygame.quit()