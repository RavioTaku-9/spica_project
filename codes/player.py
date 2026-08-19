import pygame as pg
from config import CUT_HEIGHT, RATIO_X, RATIO_Y, SCREEN_HEIGHT, SCREEN_WIDTH, scale_x, scale_y

class Player():
    def __init__(self):
        self.reset()

    @property
    def rect(self):
        return self._rect
    @rect.setter
    def rect(self, value):
        self._rect = value

    def reset(self):

        self._base_size = 16 * RATIO_X  # 基本サイズをRATIO_Xでスケーリング
        self._w = self._base_size
        self._h = self._base_size

        self._images = [
            pg.transform.smoothscale(pg.image.load(r"..\\images\\majo_side_1_16.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\majo_side_2_16.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\majo_side_1_16.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\majo_side_2_16.png").convert_alpha(), (self._w, self._h)),
        ]
        self._image = self._images[0]

     
        self._rect = pg.Rect(scale_x(5), scale_y(2), self._w, self._h)
        self._speed = scale_x(1)
        self._cnt = 0

    def update(self):
        key = pg.key.get_pressed()
        vx = 0
        vy = 0
        if key[pg.K_UP]:
            vy = -self._speed
        if key[pg.K_DOWN]:
            vy = self._speed
        if self._rect.y + vy < 0 or self._rect.y + vy > (CUT_HEIGHT - 16) * RATIO_Y:
            vy = 0
        self._rect.y += vy

        if key[pg.K_RIGHT]:
            vx = self._speed
        if key[pg.K_LEFT]:
            vx = -self._speed
        if self._rect.x + vx < 0 or self._rect.x + vx > SCREEN_WIDTH - 16 * RATIO_X:
            vx = 0
        self._rect.x += vx
        self._cnt += 1
        self._image = self._images[self._cnt // 10 % 4]

    def draw(self, screen):
        screen.blit(self._image, self._rect)
        fire_rect = self._rect.copy()
        fire_rect.x += 3 * RATIO_X  
        fire_rect.y -= 3 * RATIO_Y  
        #screen.blit(self._image_fire, fire_rect)
        leaf_rect = self._rect.copy()
        leaf_rect.x -= 3 * RATIO_X
        leaf_rect.y += 3 * RATIO_Y  
        #screen.blit(self._image_leaf, leaf_rect)
        aqua_rect = self._rect.copy()
        aqua_rect.x += 3 * RATIO_X
        aqua_rect.y += 11 * RATIO_Y
        #screen.blit(self._image_aqua, aqua_rect)



