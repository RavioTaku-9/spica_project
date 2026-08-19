import math

import pygame as pg
from config import BASE_SCREEN_WIDTH, CUT_HEIGHT, RATIO_X, RATIO_Y

class Bullet():
    def __init__(self, rect):

        self._base_size = 4 * RATIO_X
        self._w = self._base_size
        self._h = self._base_size

        x = rect.x + 16 * RATIO_X
        y = rect.y + 2 * RATIO_X

        self._image = pg.image.load(r"..\\images\\bullet.png")
        self._image = pg.transform.smoothscale(self._image, (self._w, self._h))
        self._rect = self._image.get_rect()
        self._rect.topleft = (x, y)
        self._vx = 1.2 * RATIO_X
        self._vy = 0
        self._is_alive = True
        #self._damage = [100, 34, 34, 34]  # normal, fire, leaf, aqua
        self._damage = [100, 100, 100, 100]  # normal, fire, leaf, aqua

    @property
    def rect(self):
        return self._rect
    
    @property
    def damage(self):
        return self._damage
    
    @property
    def is_alive(self):
        return self._is_alive

    @is_alive.setter
    def is_alive(self, value):
        self._is_alive = value

    def update(self):
        self._rect.x += self._vx
        self._rect.y += self._vy
        if(
            self._rect.x > 160 * RATIO_X 
            or self._rect.x < -10 * RATIO_X
        ):
            self._is_alive = False

    def draw(self, screen):
        screen.blit(self._image, self._rect)

class StarBullet(Bullet):
    def __init__(self, rect):
        super().__init__(rect)
        self._base_size = 10 * RATIO_X
        self._w = self._base_size
        self._h = self._base_size
        self._cnt = 0

        self._images = [
            pg.transform.smoothscale(pg.image.load(r"..\\images\\bullet_star_1.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\bullet_star_2.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\bullet_star_3.png").convert_alpha(), (self._w, self._h)),
        ]
        self._image = self._images[0]

        # self._image = pg.image.load(r"..\\images\\bullet_star.png")
        # self._image = pg.transform.smoothscale(self._image, (self._w, self._h))
        self._damage = [34, 100, 0, 0]  # normal, fire, leaf, aqua
        self.bullet_cnt = 0  # 弾の寿命をカウントする変数

    def update(self):
        self._rect.x += self._vx
        self._rect.y += self._vy + math.sin(self._cnt * 0.8) * 0.13 * RATIO_Y  # 波動の動き
        self.bullet_cnt += 1
        self._cnt += 1
        # 回転角度を _cnt に応じて変える
        angle = self._cnt * 0.5  # 1フレームごとに 0度回転
        rotated = pg.transform.rotate(self._images[self._cnt // 10 % 3], -angle)
        rect = rotated.get_rect(center=self._rect.center)
        self._image = rotated
        self._rect = rect

        if(
            self._rect.x > 160 * RATIO_X 
            or self._rect.x < -10 * RATIO_X
            or self.bullet_cnt > 70
        ):
            self._is_alive = False        

class FireBullet(Bullet):
    def __init__(self, rect):
        super().__init__(rect)
        self._image = pg.image.load(r"..\\images\\bullet_fire.png")
        self._image = pg.transform.smoothscale(self._image, (self._w, self._h))
        self._damage = [34, 100, 0, 0]  # normal, fire, leaf, aqua

class LeafBullet(Bullet):
    def __init__(self, rect):
        super().__init__(rect)
        self._image = pg.image.load(r"..\\images\\bullet_leaf.png")
        self._image = pg.transform.smoothscale(self._image, (self._w, self._h))
        self._damage = [34, 0, 100, 0]  # normal, fire, leaf, aqua

class AquaBullet(Bullet):
    def __init__(self, rect):
        super().__init__(rect)
        self._image = pg.image.load(r"..\\images\\bullet_aqua.png")
        self._image = pg.transform.smoothscale(self._image, (self._w, self._h))
        self._damage = [34, 0, 0, 100]  # normal, fire, leaf, aqua

class EnemyBullet(Bullet):
    def __init__(self, rect, vx= -1.5 * RATIO_X , vy=0):
        super().__init__(rect)
        self._image = pg.image.load(r"..\\images\\enemy_bullet.png")
        self._image = pg.transform.smoothscale(self._image, (self._w, self._h))
        self._vx = vx
        self._vy = vy

    def update(self):
        self._rect.x += self._vx
        self._rect.y += self._vy
        # 画面外に出たら削除
        if (self._rect.x < -1 * RATIO_X or self._rect.x > BASE_SCREEN_WIDTH * RATIO_X or 
            self._rect.y < -1 * RATIO_X or self._rect.y > CUT_HEIGHT * RATIO_X):
            self._is_alive = False