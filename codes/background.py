import pygame as pg

class Background():
    def __init__(self):
        self._image = pg.image.load(r"..\\images\\background.jpg")
        self._bg_x = 0
        self._rect = self._image.get_rect()
        self._rect.topleft = (0, 0)
    def update(self, screen_width):
        self._bg_x -= 1
        if self._bg_x <= -screen_width:
            self._bg_x = 0

    def draw(self, screen, screen_width):
        screen.blit(self._image, (self._bg_x, 0))
        screen.blit(self._image, (self._bg_x + screen_width, 0))