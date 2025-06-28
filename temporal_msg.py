import pygame
import constantes as c

class TempMsg:

    def __init__(self, duration, text, image_path):
        self.start = pygame.time.get_ticks()
        self.duration = duration
        self.text = text
        self.pos = (100, 10)
        self.font = pygame.font.Font("fonts/OETZTYP_.TTF", 15)
        self.visible = True
        self.image = pygame.image.load(image_path).convert_alpha()


    def show_msg(self, screen):
        """
        Display the temporary message on the screen.
        Checks if the message is still within its duration and blits the image and text on the screen.
        -------------------------------------------------------------------------
        Arguments:
            screen (pygame.Surface): The surface on which to draw the message.
        -------------------------------------------------------------------------
        Returns:
            None
        """
        current_time = pygame.time.get_ticks()
        if current_time - self.start <= self.duration:
            lines = self.text.split("\n")
            image_rect = self.image.get_rect(topleft=self.pos)
            screen.blit(self.image, self.pos)
            line_heigth = 0
            for line in lines:    
                render_text = self.font.render(line, True, c.RED)
                text_rect = render_text.get_rect(center=(image_rect.centerx, image_rect.midtop[1] + line_heigth + 65))
                screen.blit(render_text, text_rect)
                line_heigth += render_text.get_height()
        else:
            self.visible = False