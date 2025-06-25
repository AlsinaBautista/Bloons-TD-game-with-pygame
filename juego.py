import pygame
import pygame.scrap
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
import sounds as s
from new_round_button import *

# Al principio del archivo
#def excepthook(type, value, traceback):
#    print("ERROR NO CAPTURADO:", type, value)
#    pygame.quit()
#    sys.exit()
#
#sys.excepthook = excepthook

pygame.init() #inicializamos todos los modulos de pygame
pygame.mixer.init()
pygame.mixer.music.play(-1) #para loop, la musica esta en sounds
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
icon = pygame.image.load("imgs/icono_globos.jpeg")
pygame.display.set_icon(icon)
pygame.display.set_caption("Bloons TD")

map = Map("imgs/fondo.png")
enemies = pygame.sprite.Group()
#new_enemy = Enemy(c.ENEMY_POS, c.ENEMY_SPEED, c.ENEMY_HEALTH, c.ENEMY_IMG, c.ENEMY_PATH, False)
#enemies.add(new_enemy)

# Imagen de towers para shop
canon_img_shop = pygame.image.load("imgs/tower_shop.png").convert_alpha()
sniper_img_shop = pygame.image.load("imgs/shooter_shop.png").convert_alpha()
ship_img_shop = pygame.image.load("imgs/ship_shop.png").convert_alpha()
fast_mokey_img_shop = pygame.image.load("imgs/fast_monkey_shop.png").convert_alpha()

bullets = pygame.sprite.Group()

money_img = pygame.image.load("imgs/money.png")
money = Money(700, money_img)
life_img = pygame.image.load("imgs/life.png")
life = Life(20, life_img)

bg_shop = pygame.image.load("imgs/bg_shop.png")

# Tienda y drag (torre en mouse)
shop_canon = Shop(canon_img_shop, 795, 30, 450, money)
shop_sniper = Shop(sniper_img_shop, 885, 30, 500, money)
shop_fast_monkey = Shop(fast_mokey_img_shop, 795, 150, 200, money)
shop_ship = Shop(ship_img_shop, 885, 150, 450, money)
dragging_tower = None # Variable que indica si el jugador esta arrastrando una torre desde la tienda
towers = pygame.sprite.Group() # Grupo que contiene todas las torres colocadas en el mapa

# Imagen tacho de basura
trash_img = pygame.image.load("imgs/trash.png").convert_alpha()
trash_hover = pygame.image.load("imgs/trash_hover.png").convert_alpha()

spawn_timer = pygame.time.get_ticks()

active_msg = []

game_speed = 1
speed_button = Button(c.SPEED_BUTTON_IMG, (725, 500), 0)

grid = start_grid()

rounds_list = lr.rounds_list
round_manager = Round(rounds_list)
round_but = Gen_But(c.ROUND_BUT_IMG, (725, 500), 0)
mute_but = Gen_But(c.MUTE_BUT_IMG, (30, 500), 0)
unmute_but = Gen_But(c.UNMUTE_BUT_IMG, (80, 500), 0)
run = True
while run:
    delta_time = clock.tick(60) / 1000
    mouse_pos = pygame.mouse.get_pos() # Posicion actual del mouse
    mouse_celd_value = grid.get_value(grid.get_celd(mouse_pos)[0], grid.get_celd(mouse_pos)[1])

    for event in pygame.event.get(): #el .event.get devuelve todos los eventos (teclado, mouse, etc.)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if speed_button.is_clicked(event.pos) and not dragging_tower: #is_clicked es si el mouse esta sobre el boton, pero como esta en el if de MOUSEBUTTONDOWN funciona como un clickeo
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
            
            if round_manager.is_round_over(enemies, money) and round_manager.round < len(rounds_list): #si termina la ronda y todavia quedan mas rondas pasa a la otra ronda
                if round_but.is_clicked(event.pos):
                    round_manager.new_round(current_time, money)

            if mute_but.is_clicked(event.pos):
                pygame.mixer.music.stop()
            if unmute_but.is_clicked(event.pos):
                pygame.mixer.music.play(-1)

            if mouse_celd_value in [3, 4, 5, 6]:
                for tower in towers:
                    if grid.get_celd(tower.pos) == grid.get_celd(mouse_pos) and tower.level < tower.max_level:
                        tower.selected = True
                        tower.showing_button = True
                    else:
                        tower.selected = False
            for tower in towers:
                if tower.selected and tower.upgrade_button.is_clicked(mouse_pos):
                    tower.upgrade(money, mouse_celd_value)
                    tower.update_img(tower)

            if mouse_celd_value not in (3, 4, 5, 6): #las mejoras solo son para torres
                for tower in towers:
                    if tower.selected and tower.showing_button:
                        tower.selected = False
                        tower.showing_button = False

        if event.type == pygame.QUIT:
            run = False #cierra
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            dragging_tower = shop_canon.shop_items(dragging_tower, Cannon, screen, towers, all_sprites, pos, active_msg, game_speed, grid)
            dragging_tower = shop_sniper.shop_items(dragging_tower, Sniper, screen, towers, all_sprites, pos, active_msg, game_speed, grid)
            dragging_tower = shop_fast_monkey.shop_items(dragging_tower, Basic, screen, towers, all_sprites, pos, active_msg, game_speed, grid)
            dragging_tower = shop_ship.shop_items(dragging_tower, Ship, screen, towers, all_sprites, pos, active_msg, game_speed, grid)

    map.draw_background(screen)
    #map.draw_celds(screen, c.WHITE, c.CELD)

    current_time = pygame.time.get_ticks()
    
    round_manager.update(current_time, game_speed, enemies, all_sprites)
    
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

    if not round_manager.is_round_over(enemies, money):
        speed_button.draw(screen)
    else:
        round_but.draw(screen)
    mute_but.draw(screen)
    unmute_but.draw(screen)
    # Dibujo de las torres colocadas
    for tower in towers:
        screen.blit(tower.img, (tower.pos[0] - tower.img.get_width()//2, tower.pos[1] - tower.img.get_height()//2))
        grid.update_grid(tower)
        #tower.draw_scope(screen)
    
    # Dibujo de la tienda
    inventory_height = c.HEIGHT
    inventory_rect = pygame.Rect(c.WIDTH - c.INVENTORY_WIDTH, 0, c.INVENTORY_WIDTH, inventory_height)
    bg_shop_scaled = pygame.transform.scale(bg_shop, (inventory_rect.width, inventory_rect.height))
    screen.blit(bg_shop_scaled, inventory_rect.topleft)

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

    if life.game_over():
        #black_screen = pygame.Surface((c.WIDTH, c.HEIGHT), pygame.SRCALPHA)
        #black_screen.fill((0,0,0,180))
        ##screen.blit(black_screen, (0,0))
        pygame.mixer.music.stop()
        game_over.play()
        #font = pygame.font.Font('fonts/OETZTYP_.TTF', 48)
        defeat_img_rect = c.DEFEAT_IMG.get_rect(center=(c.WIDTH // 2, c.HEIGHT // 2))
        screen.blit(c.DEFEAT_IMG, defeat_img_rect)
        #text = font.render("GAME OVER", True, c.RED)
        #text_rect = text.get_rect(center=(c.WIDTH // 2, c.HEIGHT // 2))
        #screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(5000)
        run = False
    
    if round_manager.round == 50: #si es la ultima ronda se cierra con sondido
        if round_manager.is_round_over(enemies, money):
            black_screen = pygame.Surface((c.WIDTH, c.HEIGHT), pygame.SRCALPHA)
            black_screen.fill((0, 0, 0, 180))
            screen.blit(black_screen, (0,0))
            victory_img_rect = c.VICTORY_IMG.get_rect(center=(c.WIDTH // 2, c.HEIGHT // 2))
            screen.blit(c.VICTORY_IMG, victory_img_rect)
            s.victory_sound.play()
            pygame.display.update()
            pygame.time.delay(5000)
            pygame.quit()
            sys.exit()
    for m in active_msg[:]:
        if m.visible:
            m.show_msg(screen)
        else:
            active_msg.remove(m)

    #clock.tick(60)
    speed_button.hover(screen, mouse_pos)

    round_manager.draw_text(screen)

    if not round_manager.is_active and not round_manager.pending_enemies and not round_manager.reward_given:
        money.add_money(round_manager.reward[round_manager.round - 1])
        round_manager.reward_given = True
 
    for tower in towers:
        if tower.selected:
            #scope_surface= tower.draw_scope()
            #screen.blit(scope_surface, tower.rect)
            tower.update_upgrade_button_pos()
            if tower.level < 3:
                color = (255, 255, 255) if money.cant_total > tower.costs[tower.level] else (255, 0, 0)
                tower.upgrade_button.draw(screen, f'${tower.costs[tower.level]}', color)
                tower.upgrade_button.hover(screen, mouse_pos)
        #print(tower.att_speed)
        #print(tower.damage)
        #print(grid)
    pygame.display.update()

pygame.quit()