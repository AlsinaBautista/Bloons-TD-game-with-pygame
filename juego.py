import pygame
import constantes as c
from map import Map
from enemy import Enemy
from tower import Tower
from bullet import Bullet
import sys
from money import Money

# Al principio del archivo
def excepthook(type, value, traceback):
    print("ERROR NO CAPTURADO:", type, value)
    pygame.quit()
    sys.exit()

sys.excepthook = excepthook

pygame.init()

screen = pygame.display.set_mode((c.width, c.height))
icon = pygame.image.load("imgs/icono_globos.jpeg")
pygame.display.set_icon(icon)
pygame.display.set_caption("Bloons TD")

map = Map("imgs/fondo.png")
enemies = pygame.sprite.Group()
new_enemy = Enemy(c.enemy_pos, c.enemy_speed, c.enemy_health, c.enemy_img, c.enemy_path)
enemies.add(new_enemy)

# Imagen de torre dummy (puede ser reemplazada luego)
tower_img = pygame.image.load("imgs/towerupr.png").convert_alpha()

# Crear una torre de prueba en el centro de la pantalla
test_tower = Tower(pos=(470, c.height//2), scope=100, damage=50, att_speed=500, target=None, price=50, image=tower_img)
bullets = pygame.sprite.Group()
bullet = test_tower.shoot(enemies)
if bullet:
    bullets.add(bullet)

money_img = pygame.image.load("imgs/money.png")
money = Money(750, money_img)

spawn_timer = pygame.time.get_ticks()
enemy_spawn_interval = 300  # milisegundos
enemy_count = 0
max_enemies = 30

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    map.draw_background(screen)
    map.draw_celds(screen, c.white, c.celd)

    current_time = pygame.time.get_ticks()

    if enemy_count < max_enemies and current_time - spawn_timer >= enemy_spawn_interval:
        new_enemy = Enemy(c.enemy_pos, c.enemy_speed, c.enemy_health, c.enemy_img, c.enemy_path)
        enemies.add(new_enemy)
        enemy_count += 1
        spawn_timer = current_time 
    
    enemies.update(money)
    enemies.draw(screen)

    test_tower.draw_scope(screen) 
    screen.blit(test_tower.img, (test_tower.pos[0] - test_tower.img.get_width()//2,
                                test_tower.pos[1] - test_tower.img.get_height()//2))
    
    if test_tower.bullet_active and not test_tower.bullet_active.alive():
        test_tower.bullet_active = None

    new_bullet = test_tower.shoot(enemies)
    if new_bullet:
        bullets.add(new_bullet)
    
    bullets.update()
    bullets.draw(screen)

    money.draw(screen)

    pygame.display.update()

pygame.quit()
