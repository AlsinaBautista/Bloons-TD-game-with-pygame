import pygame

class Map:
    def __init__(self, background_path):
        self.background = pygame.image.load(background_path).convert()

    def draw_background(self, screen):
        screen.blit(self.background, (0, 0))

    def draw_celds(self, screen, color, celd_size):
        for x in range(0, screen.get_width(), celd_size):
            pygame.draw.line(screen, color, (x, 0), (x, screen.get_height()))
        for y in range(0, screen.get_height(), celd_size):
            pygame.draw.line(screen, color, (0, y), (screen.get_width(), y))


