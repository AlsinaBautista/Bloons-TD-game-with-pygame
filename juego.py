import pygame
import constantes as c
from map import Map
from enemy import Enemy

pygame.init()

screen = pygame.display.set_mode((c.width, c.height))
icono = pygame.image.load("icono_globos.jpeg")
pygame.display.set_icon(icono)
pygame.display.set_caption("Bloons TD")

map = Map("fondo.png")
enemy = Enemy(c.enemy_pos, c.enemy_speed, c.enemy_health, c.enemy_img, c.enemy_path)

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

    pygame.display.update()

pygame.quit()
