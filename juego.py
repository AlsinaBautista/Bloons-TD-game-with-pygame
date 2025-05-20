import pygame

pygame.init()

# Creando pantalla
screen = pygame.display.set_mode((1250,600))

# Cargar el icono (debe ser una imagen tipo .png o .jpg)
icono = pygame.image.load("icono_globos.jpeg")
pygame.display.set_icon(icono)

# Cargar el nombre del juego
pygame.display.set_caption("PEPE")

# Pintar fondo de marron
marron = (207, 168, 19)
screen.fill(marron)

# Cargar imagen para el fondo
fondo = pygame.image.load("fondo.jpeg")
screen.blit(fondo, (0,0))

# Agregar sombra al inventario
borde_inventario = (171, 138, 13)
pygame.draw.line(screen, borde_inventario, (1025,0), (1025,600), 5)

# Agregar bordes de botones de la tienda
mitad_tienda = (1250 - 1025) / 2 + 1025
pygame.draw.line(screen, borde_inventario, (mitad_tienda, 0), (mitad_tienda, 600), 1)

ancho = 600
while ancho != 0:
    pygame.draw.line(screen, borde_inventario, (1025, ancho), (1250, ancho), 1)
    ancho -= 100


# Cargar tienda
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()