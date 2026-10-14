import pygame as pg
from config import CUT_HEIGHT, RATIO_Y, SCREEN_WIDTH, SCREEN_HEIGHT, IMAGE_DIR, RATIO_X, RATIO_Y

import random

class Background():
    def __init__(self, bg_index = 0):
        self._images =[pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "background_night_town.png").convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
                       pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "background_twilignt_2.png").convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
                       pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "background_snow_mountain_1.png").convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
                       pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "background_day_town.png").convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
                       pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "background_musium_1.png").convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
                       ]
        self._bg_index = bg_index
        self._image = self._images[self._bg_index]  # bg_indexを使用
        self._bg_x = 0
        self._rect = self._image.get_rect()
        self._rect.topleft = (0, 0)
        self._change_cooldown = 0  # クールダウンタイマー
        
    def next_background(self):
        if self._change_cooldown > 0:
            return  # クールダウン中は変更しない
        self._bg_index = (self._bg_index + 1) % len(self._images)
        self._image = self._images[self._bg_index]
        self._change_cooldown = 30  # 0.5秒
    
    def prev_background(self):
        if self._change_cooldown > 0:
            return  # クールダウン中は変更しない
        self._bg_index = (self._bg_index - 1) % len(self._images)
        self._image = self._images[self._bg_index]
        self._change_cooldown = 30  # 0.5秒
    
    @property
    def bg_index(self):
        return self._bg_index

    def update(self, screen_width):
        # クールダウンを減らす
        if self._change_cooldown > 0:
            self._change_cooldown -= 1                       
        self._bg_x -= 0.5
        if self._bg_x <= -screen_width:
            self._bg_x = 0

    def draw(self, screen, screen_width):
        # 下のステータスバーの分だけ背景を上にしている
        cut_h = CUT_HEIGHT * RATIO_Y
        clip_rect = pg.Rect(0, 0, screen_width, cut_h)
        screen.set_clip(clip_rect)
        screen.blit(self._image, (self._bg_x, -70))
        screen.blit(self._image, (self._bg_x + screen_width, -70))
        screen.set_clip(None)