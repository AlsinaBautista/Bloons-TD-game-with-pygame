import pygame
import sys
from menu import Menu
import constantes as c

pygame.init()

hand = pygame.cursors.Cursor((0,0), c.CURSOR_HAND_IMG)
arrow = pygame.cursors.Cursor((0,0), c.CURSOR_IMG)
# Crear ventana

screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("Menu Inicial")

menu = Menu()

background = pygame.image.load("imgs/background-menu.png").convert()

while True:
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(background, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    # Verificamos si el mouse esta en el boton
    if menu.boton_rect.collidepoint(mouse_pos):
        pygame.mouse.set_cursor(hand)
    else:
        pygame.mouse.set_cursor(arrow)

    menu.draw_button(screen, mouse_pos)


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if menu.boton_rect.collidepoint(evento.pos):
                import juego
                #print("Apreto")
                pygame.quit()
                sys.exit()

    pygame.display.flip()
