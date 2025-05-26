import pygame
import constantes as c
from map import Map
from enemy import Enemy
from tower import Tower
from bullet import Bullet
import sys
from money import Money
from life import Life
from shop import Shop 

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
tower_img = pygame.image.load("imgs/tower.png").convert_alpha()

# Crear una torre de prueba en el centro de la pantalla
test_tower = Tower(pos=(470, c.height//2), scope=200, damage=1, att_speed=500, target=None, price=50, image=tower_img)

bullets = pygame.sprite.Group()
bullet = test_tower.shoot(enemies)
if bullet:
    bullets.add(bullet)

money_img = pygame.image.load("imgs/money.png")
money = Money(750, money_img)
life_img = pygame.image.load("imgs/life.png")
life = Life(20, life_img)

# Tienda y drag (torre en mouse)
shop_item = Shop(tower_img, 810, 10, 300, money)
dragging_tower = None # Variable que indica si el jugador esta arrastrando una torre desde la tienda
towers = pygame.sprite.Group() # Grupo que contiene todas las torres colocadas en el mapa

spawn_timer = pygame.time.get_ticks()
enemy_spawn_interval = 300  # milisegundos
enemy_count = 0
max_enemies = 30

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            
            if dragging_tower is None:
                # Si no estas arrastrando una torre, revisamos si hiciste clic en la tienda
                if shop_item.is_clicked(pos):
                    if money.cant_total >= shop_item.price:
                        dragging_tower = Tower(pos=(470, c.height//2), scope=200, damage=1, att_speed=500, target=None, price=50, image=tower_img)
                    else:
                        print("No tenes suficiente dinero")
            else:
                # Si ya estas arrastrando una torre, al hacer clic se coloca en el mapa
                pos = (pos[0] // c.celd * c.celd + c.celd // 2, pos[1] // c.celd * c.celd + c.celd // 2) # Redondea la posicion al centro de la celda
                if not c.grid[pos[1] // c.celd][pos[0] // c.celd]: # Verifica si la celda esta vacia
                # Si la celda esta vacia, coloca la torre
                    dragging_tower.set_tower(*pos) # Posiciona la torre en el lugar del clic
                    money.spend_money(shop_item.price)
                    towers.add(dragging_tower) # Agrega la torre al grupo de torres
                    dragging_tower = None
                else:
                    print("No se puede colocar la torre aqui, la celda esta ocupada")

    map.draw_background(screen)
    map.draw_celds(screen, c.white, c.celd)

    current_time = pygame.time.get_ticks()

    if enemy_count < max_enemies and current_time - spawn_timer >= enemy_spawn_interval:
        new_enemy = Enemy(c.enemy_pos, c.enemy_speed, c.enemy_health, c.enemy_img, c.enemy_path)
        enemies.add(new_enemy)
        enemy_count += 1
        spawn_timer = current_time 
    
    enemies.update(money,life)
    enemies.draw(screen)

    # Torre de prueba
    test_tower.draw_scope(screen) 
    screen.blit(test_tower.img, (test_tower.pos[0] - test_tower.img.get_width()//2,
                                test_tower.pos[1] - test_tower.img.get_height()//2))
    
    if test_tower.bullet_active and not test_tower.bullet_active.alive():
        test_tower.bullet_active = None

    new_bullet = test_tower.shoot(enemies)
    if new_bullet:
        bullets.add(new_bullet)
    # Torres colocadas desde la tienda
    for tower in towers:
        bullet = tower.shoot(enemies)
        if bullet:
            bullets.add(bullet)

    bullets.update()
    bullets.draw(screen)

    money.draw(screen)
    life.draw(screen)

    # Dibujo de la tienda
    inventory_width = int(c.width * 0.2) # La tienda ocupa el 20% del ancho total
    inventory_height = c.height
    inventory_rect = pygame.Rect(c.width - inventory_width, 0, inventory_width, inventory_height)
    pygame.draw.rect(screen, (191,158,83), inventory_rect) # Dibuja el fondo de la tienda
    shop_item.draw(screen) # Dibuja la torre disponible en la tienda 

    # Dibujo de las torres colocadas
    for tower in towers:
        screen.blit(tower.img, (tower.pos[0] - tower.img.get_width()//2, tower.pos[1] - tower.img.get_height()//2))
        tower.draw_scope(screen)
    
    # Dar el efecto de que el mouse lleva al item del cañon
    if dragging_tower is not None:
        mouse_pos = pygame.mouse.get_pos() # Posicion actual del mouse
        dragging_tower.set_tower(*mouse_pos) # Actualiza la posicion de la torre arrastrada
        screen.blit(dragging_tower.img, (mouse_pos[0] - dragging_tower.img.get_width()//2, mouse_pos[1] - dragging_tower.img.get_height()//2)) # Dibuja la imagen de la torre en la pantalla, de forma que su centro este exactamente donde esta el mouse

    if life.cant_total <= 0:
        font = pygame.font.SysFont('showcardgothic', 48)
        text = font.render("GAME OVER", True, (255, 255, 255))
        text_rect = text.get_rect(center=(c.width // 2, c.height // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        run = False

    pygame.display.update()

pygame.quit()
