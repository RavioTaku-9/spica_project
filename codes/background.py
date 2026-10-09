import pygame as pg
from config import BACKGROUND_IMAGE, CUT_HEIGHT, RATIO_Y, SCREEN_WIDTH, SCREEN_HEIGHT, BASE_SCREEN_WIDTH, BASE_SCREEN_HEIGHT, scale_x, scale_y


class Background():
    def __init__(self):
        self._image = pg.image.load(BACKGROUND_IMAGE).convert_alpha()
        # 背景も同じ基準サイズに揃える
        base_w = scale_x(BASE_SCREEN_WIDTH)
        base_h = scale_y(BASE_SCREEN_HEIGHT)
        self._image = pg.transform.smoothscale(self._image, (base_w, base_h))
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