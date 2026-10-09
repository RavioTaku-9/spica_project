import pygame as pg
from config import CUT_HEIGHT, RATIO_Y, SCREEN_WIDTH, SCREEN_HEIGHT, IMAGE_DIR, RATIO_X, RATIO_Y

class Background():
    def __init__(self):
        self._image = pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "background_night_town.png").convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self._bg_x = 0
        self._rect = self._image.get_rect()
        self._rect.topleft = (0, 0)
    def update(self, screen_width):
        self._bg_x -= 0.5
        if self._bg_x <= -screen_width:
            self._bg_x = 0

    def draw(self, screen, screen_width):
        cut_h = CUT_HEIGHT * RATIO_Y

        clip_rect = pg.Rect(0, 0, screen_width, cut_h)
        screen.set_clip(clip_rect)

        screen.blit(self._image, (self._bg_x, -70))
        screen.blit(self._image, (self._bg_x + screen_width, -70))

        screen.set_clip(None)