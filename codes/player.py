import pygame as pg
from config import SCREEN_WIDTH, SCREEN_HEIGHT

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
        self._images = [
            pg.image.load(r"..\\images\\majo_side_1_100.png"),
            pg.image.load(r"..\\images\\majo_side_2_100.png"),
            pg.image.load(r"..\\images\\majo_side_1_100.png"),
            pg.image.load(r"..\\images\\majo_side_3_100.png")
        ]
        self._image = self._images[0]

        self._image_fire = pg.image.load(r"..\\images\\bullet_fire.png")
        self._image_leaf = pg.image.load(r"..\\images\\bullet_leaf.png")
        self._image_aqua = pg.image.load(r"..\\images\\bullet_aqua.png")

        self._rect = pg.Rect(250, 200, 100,100)
        self._speed = 10
        self._cnt = 0

    def update(self):
        key = pg.key.get_pressed()
        vx = 0
        vy = 0
        if key[pg.K_UP]:
            vy = -self._speed
        if key[pg.K_DOWN]:
            vy = self._speed
        if self._rect.y + vy < 0 or self._rect.y + vy > SCREEN_HEIGHT - 350:
            vy = 0
        self._rect.y += vy

        if key[pg.K_RIGHT]:
            vx = self._speed
        if key[pg.K_LEFT]:
            vx = -self._speed
        if self._rect.x + vx < 0 or self._rect.x + vx > SCREEN_WIDTH - 100:
            vx = 0
        self._rect.x += vx
        self._cnt += 1
        self._image = self._images[self._cnt // 10 % 4]

    def draw(self, screen):
        screen.blit(self._image, self._rect)
        fire_rect = self._rect.copy()
        fire_rect.x += 30
        fire_rect.y -= 30  # y座標を100小さく
        #screen.blit(self._image_fire, fire_rect)
        leaf_rect = self._rect.copy()
        leaf_rect.x -= 30
        leaf_rect.y += 30  
        #screen.blit(self._image_leaf, leaf_rect)
        aqua_rect = self._rect.copy()
        aqua_rect.x += 30
        aqua_rect.y += 110  
        #screen.blit(self._image_aqua, aqua_rect)



