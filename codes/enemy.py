from logging import config
import math

import pygame as pg
import random
from config import  CUT_HEIGHT, RATIO_X, RATIO_Y, BASE_SCREEN_WIDTH, BASE_SCREEN_HEIGHT, SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy():
    def __init__(self):
        x = BASE_SCREEN_WIDTH * RATIO_X * random.randint(1, 2)
        y = CUT_HEIGHT * RATIO_Y * random.randint(1, 8) // 10
        self._base_size = 16 * RATIO_X  # 基本サイズをRATIO_Xでスケーリング
        self._w = self._base_size
        self._h = self._base_size

        self._images = [
            pg.transform.smoothscale(pg.image.load(r"..\\images\\WBdolphin_1_100.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\WBdolphin_2_100.png").convert_alpha(), (self._w, self._h)),
            
        ]
        self._image = self._images[0]
        self._rect = pg.Rect(x,y, self._w, self._h)
        self._vx = random.uniform(1, 1) * 0.5 * RATIO_X
        self._vy = random.uniform(1, 1) * 0.5 * RATIO_Y
        self._cnt = 0
        #self._maxhp = 100
        #self._hp = 100
        self._maxhp = [100, 0, 0, 0] #normal, fire, leaf, aqua
        self._hp = [100, 0, 0, 0]
        self._is_alive = True
        self._etype = "normal"  # normal, fire, leaf, aqua
        self._can_shoot = True

    @property
    def is_alive(self):
        return self._is_alive
    
    @is_alive.setter
    def is_alive(self, value):
        self._is_alive = value
    
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def maxhp(self):
        return self._maxhp

    @property
    def rect(self):
        return self._rect
    @rect.setter
    def rect(self, value):
        self._rect = value

    @property
    def vx(self):
        return self._vx
    @vx.setter
    def vx(self, value):
        self._vx = value

    def update(self):
        self._rect.x -= self._vx
        self._cnt += 1
        self._image = self._images[self._cnt // 10 % 4]
        if (
            self._rect.x < -10 * RATIO_X
            or self._rect.x > SCREEN_WIDTH + 10 * RATIO_X
            or self._rect.y < -10 * RATIO_Y
            or self._rect.y > SCREEN_HEIGHT + 10 * RATIO_Y
        ):
            self._is_alive = False
    
    def draw(self, screen):
        screen.blit(self._image, self._rect)

class EnemyLeaf(Enemy):
    def __init__(self):
        super().__init__()
        self._images = [pg.transform.smoothscale(pg.image.load(r"..\\images\\enemy_leaf.png").convert_alpha(), (self._w, self._h))] * 4
        # self._images = [pg.image.load(r"..\\images\\enemy_leaf.png")] * 4  # 4枚同じ画像でリストを作る
        self._image = self._images[0]
        self._etype = "leaf"
        self._maxhp = [0, 0, 100, 0]#normal, fire, leaf, aqua
        self._hp = [0, 0, 100, 0]#normal, fire, leaf, aqua

    def update(self):
        super().update() 
        # 波動の動き
        self._rect.y += int(math.sin(self._cnt * 0.1) * 3 * RATIO_Y)

class EnemyAqua(Enemy):
    def __init__(self):
        super().__init__()
        self._images = [pg.transform.smoothscale(pg.image.load(r"..\\images\\enemy_aqua.png").convert_alpha(), (self._w, self._h))] * 4  # 4枚同じ画像でリストを作る
        self._image = self._images[0]
        self._etype = "aqua"
        self._maxhp = [0, 0, 0, 100]#normal, fire, leaf, aqua
        self._hp = [0, 0, 0, 100]#normal, fire, leaf, aqua

class EnemyFire(Enemy):
    def __init__(self):
        super().__init__()
        self._images = [pg.transform.smoothscale(pg.image.load(r"..\\images\\enemy_fire_16.png").convert_alpha(), (self._w, self._h))] * 4  # 4枚同じ画像でリストを作る
        self._image = self._images[0]
        self._etype = "fire"
        self._maxhp = [0, 100, 0, 0]#normal, fire, leaf, aqua
        self._hp = [0, 100, 0, 0]#normal, fire, leaf, aqua

class BombEffect():
    def __init__(self, rect, effects):
        self._base_size = 16 * RATIO_X  # 基本サイズをRATIO_Xでスケーリング
        self._w = self._base_size
        self._h = self._base_size
        self._images = [
            pg.transform.smoothscale(pg.image.load(r"..\\images\\bomb_0_16.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\bomb_1_16.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\bomb_2_16.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\bomb_3_16.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\bomb_4_16.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\bomb_5_16.png").convert_alpha(), (self._w, self._h))
        ]
        self._image = self._images[0]
        self._effects = effects
        self._rect = rect
        self._cnt = 0

    def update(self):
        self._cnt += 1
        idx = self._cnt // 5
        if idx <= 5:
            self._image = self._images[idx]
        else:
            self._effects.remove(self)

    def draw(self, screen):
        screen.blit(self._image, self._rect)

class BombEffectStar(BombEffect):
    def __init__(self, rect, effects):
        super().__init__(rect, effects)
        self._base_size = 16 * RATIO_X  # 基本サイズをRATIO_Xでスケーリング
        self._w = self._base_size
        self._h = self._base_size
        self._images = [
            pg.transform.smoothscale(pg.image.load(r"..\\images\\bomb_0_16.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\bomb_1_16.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\bomb_star_2_16.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\bomb_star_3_16.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\bomb_star_4_16.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\bomb_star_5_16.png").convert_alpha(), (self._w, self._h))
        ]
        self._image = self._images[0]

class EnemyFactory():
    def create(self, etype):
        if etype == "normal":
            return Enemy()
        elif etype == "leaf":
            return EnemyLeaf()
        elif etype == "aqua":
            return EnemyAqua()
        elif etype == "fire":
            return EnemyFire()
        return None
    
    def random_create(self):
        #etypes = random.choice(["leaf", "fire", "aqua"])
        etypes = random.choice(["fire"])
        return self.create(etypes)