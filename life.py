import pygame

class Life:

    def __init__(self, cant_inicial, image):
        self.cant_inicial = cant_inicial
        self.cant_total = cant_inicial
        self.img = image
        self.rect = image.get_rect(center=(20, 50))

    def lose_life(self, cant):
        """
        Lose a specified amount of life.
        Decreases the total life count by the specified amount.
        -------------------------------------------------------------------------
        Arguments:
            cant (int): The amount of life to lose.
        -------------------------------------------------------------------------
        Returns:
            None
        """
        self.cant_total -= cant
    
    def draw(self, screen):
        """
        Draw the life indicator on the screen.
        Blits the life image and the current life count on the screen.
        -------------------------------------------------------------------------
        Arguments:
            screen (pygame.Surface): The surface on which to draw the life indicator.
        -------------------------------------------------------------------------
        Returns:
            None
        """
        screen.blit(self.img, self.rect)
        font = pygame.font.Font("fonts/OETZTYP_.TTF", 24)
        text = font.render(str(self.cant_total), True, (255, 255, 255))
        screen.blit(text, (self.rect.right + 10, self.rect.centery - 10))

    def game_over(self):
        """
        Checks if the total life count is less than or equal to zero.
        -------------------------------------------------------------------------
        Returns:
            bool: True if the game is over (life count is zero or less), False otherwise.
        """
        return self.cant_total <= 0