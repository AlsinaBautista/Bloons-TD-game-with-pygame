import pygame
from constantes import *
from money import *
from temporal_msg import TempMsg
from tower import *
from grid import *

class Shop:
    def __init__(self, img_tower, x, y, price, money):
        self.img_tower = img_tower
        # Crear triangulo en la imagen para detectar clics
        self.rect = self.img_tower.get_rect(topleft=(x, y)) # (x, y) donde se va mostrar el cañon en la tienda
        self. price = price
        self.money = money # para acceder al dinero del jugador
    
    def draw(self, screen):
        screen.blit(self.img_tower, self.rect)
        color = c.BROWN if self.money.cant_total >= self.price else (255, 0, 0) # Si el jugador tiene suficiente dinero
        screen.blit(pygame.font.Font("fonts/OETZTYP_.TTF", 20).render(f"${self.price}", True, color), (self.rect.x + 12, self.rect.y + self.rect.height - 28))

    def is_clicked(self, pos):
        # Si el jugador hizo clic sobre el cañon de la tienda, devuelve true
        return self.rect.collidepoint(pos) # pos es la posicion del mouse cuando se hace el clic

    def shop_items(self, dragging_tower, tower_class, screen, towers, all_sprites, pos, active_msg, game_speed, grid):
        if dragging_tower is None:
            if self.is_clicked(pos):
                if self.money.cant_total >= self.price:
                    dragging_tower = tower_class(pos=(470, c.HEIGHT // 2), game_speed=game_speed)
                    if pos[0] <= screen.get_width() - c.INVENTORY_WIDTH:
                        dragging_tower.draw_scope()
                else:
                    msg = TempMsg(1000, "No tienes\nsuficiente dinero", "imgs/msg.png")
                    active_msg.append(msg)
        else:
            try:
                if pos[0] < c.WIDTH - c.INVENTORY_WIDTH:
                    pos_grid = (pos[0] // c.CELD * c.CELD + c.CELD // 2, pos[1] // c.CELD * c.CELD + c.CELD // 2)
                    if not dragging_tower.water:
                        if grid[pos[1] // c.CELD][pos[0] // c.CELD] == 0 and pos[0] < c.WIDTH - c.INVENTORY_WIDTH:
                            dragging_tower.set_tower(*pos_grid)
                            self.money.spend_money(self.price)
                            towers.add(dragging_tower)
                            all_sprites.add(dragging_tower)
                            dragging_tower = None
                        else:
                            msg = TempMsg(1000, "No puedes colocar\nuna torre en\nese lugar", "imgs/msg.png")
                            active_msg.append(msg)
                    elif dragging_tower.water:
                        if grid[pos[1] // c.CELD][pos[0] // c.CELD] == 2 and pos[0] < c.WIDTH - c.INVENTORY_WIDTH:
                            dragging_tower.set_tower(*pos_grid)
                            self.money.spend_money(self.price)
                            towers.add(dragging_tower)
                            all_sprites.add(dragging_tower)
                            dragging_tower = None
                        else:
                            msg = TempMsg(1000, "No puedes colocar\nuna torre en\nese lugar", "imgs/msg.png")
                            active_msg.append(msg)
                    else:
                        msg = TempMsg(1000, "No puedes colocar\nuna torre en\nese lugar", "imgs/msg.png")
                        active_msg.append(msg)
            except IndexError:
                msg = TempMsg(1000, "No puedes colocar\nuna torre en\nese lugar", "imgs/msg.png")
                active_msg.append(msg)

        return dragging_tower

    def draw_trash(screen, trash_img, trash_hover, mouse_pos):
        screen.blit(trash_img, (900, 450)) # Dibuja la imagen en el pixel (900, 450)
        trash_rect = trash_img.get_rect(topleft=(900, 450)) # Crea un rectangulo del tamaño de la imagen y lo posiciona con la esquina superior izquierda en (900, 450)
        # Detectar si el mouse esta sobre el boton
        if trash_rect.collidepoint(mouse_pos):
            screen.blit(trash_hover, (900, 450))
        return trash_rect