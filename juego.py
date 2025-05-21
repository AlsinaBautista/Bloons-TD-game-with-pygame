import pygame
import constantes as c
from map import Map
from enemy import Enemy
from tower import Tower

pygame.init()

screen = pygame.display.set_mode((c.width, c.height))
icono = pygame.image.load("TP_Final/icono_globos.jpeg")
pygame.display.set_icon(icono)
pygame.display.set_caption("Bloons TD")

map = Map("TP_Final/fondo.png")
enemy = Enemy(c.enemy_pos, c.enemy_speed, c.enemy_health, c.enemy_img, c.enemy_path)

# Imagen de torre dummy (puede ser reemplazada luego)
tower_img = pygame.image.load("TP_Final/tower.png")

# Crear una torre de prueba en el centro de la pantalla
test_tower = Tower(pos=(c.width//2, c.height//2), scope=100, damage=1, att_speed=1, target=None, price=50, image=tower_img)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # No uses screen.fill si ya vas a dibujar un fondo encima
    map.draw_background(screen)
    map.draw_celds(screen, c.white, c.celd)

    enemy.move()
    enemy.draw(screen)

    test_tower.draw_scope(screen)  # Esto dibuja el círculo de alcance
    screen.blit(test_tower.img, (test_tower.pos[0] - test_tower.img.get_width()//2,
                                test_tower.pos[1] - test_tower.img.get_height()//2))
    print(test_tower.enemies_in_range(enemy.pos))

    pygame.display.update()

pygame.quit()
