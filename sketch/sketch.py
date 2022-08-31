import pygame
from pygame.rect import Rect
from pygame.color import Color
from pygame.surface import Surface
from pygame.locals import QUIT, KEYDOWN, K_RETURN, K_ESCAPE
from enum import Enum


class Colour(Enum):
    BLACK = Color(0, 0, 0)
    WHITE = Color(255, 255, 255)
    RED = Color(255, 0, 0)
    GREEN = Color(0, 255, 0)
    BLUE = Color(0, 0, 255)
    YELLOW = Color(255, 255, 0)
    PINK = Color(255, 0, 255)
    CYAN = Color(0, 255, 255)


class Window:
    """Class for drawing shapes onto a screen"""

    def __init__(self, width: int, height: int):
        pygame.init()
        pygame.display.set_caption("Sketch")
        self.screen = pygame.display.set_mode((width, height))
        self.background = Surface((width, height))
        self.background.fill(Colour.WHITE.value)
        self.screen.blit(self.background, (0, 0))

    def circle(self, colour: (int, int, int), centre: (int, int), radius: int):
        """Draws a circle onto the screen."""
        pygame.draw.circle(self.screen, colour, centre, radius)

    def square(self, colour: (int, int, int), centre: (int, int), width: int):
        """Draws a square onto the screen."""
        tl = tuple(map(lambda x: x - width // 2, centre))
        rect = Rect(tl, (width, width))
        pygame.draw.rect(self.screen, colour, rect)

    def rectangle(self, colour: (int, int, int), topleft: (int, int), width: int, height: int):
        """Draws a rectangle onto the screen."""
        rect = Rect(topleft, (width, height))
        pygame.draw.rect(self.screen, colour, rect)

    def display(self):
        """Displays the screen with all shapes drawn on."""

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_RETURN:
                        pygame.image.save(self.screen, "image.JPEG")
            pygame.display.flip()

        pygame.quit()
