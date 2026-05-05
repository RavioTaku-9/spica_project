import pygame as pg
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy():
    def __init__(self):
        x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 200)
        y = random.randint(50, SCREEN_HEIGHT - 400)
        self._images = [
            pg.image.load(r"..\\images\\WBdolphin_1_100.png"),
            pg.image.load(r"..\\images\\WBdolphin_2_100.png"),
            pg.image.load(r"..\\images\\WBdolphin_3_100.png"),
            pg.image.load(r"..\\images\\WBdolphin_2_100.png")
        ]
        self._image = self._images[0]
        self._rect = pg.Rect(x,y, 100, 100)
        self._vx = 8
        self._vy = random.uniform(-1,-4)
        self._cnt = 0
        #self._maxhp = 100
        #self._hp = 100
        self._maxhp = [100, 0, 0, 0] #normal, fire, leaf, aqua
        self._hp = [100, 0, 0, 0]
        self._is_alive = True
        self._etype = "normal"  # normal, fire, leaf, aqua

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
        if self._rect.x < -100 or self._rect.x > SCREEN_WIDTH + 100 or self._rect.y < -100 or self._rect.y > SCREEN_HEIGHT + 100:
            self._is_alive = False
    
    def draw(self, screen):
        screen.blit(self._image, self._rect)

class EnemyLeaf(Enemy):
    def __init__(self):
        super().__init__()
        self._images = [pg.image.load(r"..\\images\\enemy_leaf.png")] * 4  # 4枚同じ画像でリストを作る
        self._image = self._images[0]
        self._etype = "leaf"
        self._maxhp = [0, 0, 100, 0]#normal, fire, leaf, aqua
        self._hp = [0, 0, 100, 0]#normal, fire, leaf, aqua

class EnemyAqua(Enemy):
    def __init__(self):
        super().__init__()
        self._images = [pg.image.load(r"..\\images\\enemy_aqua.png")] * 4  # 4枚同じ画像でリストを作る
        self._image = self._images[0]
        self._etype = "aqua"
        self._maxhp = [0, 0, 0, 100]#normal, fire, leaf, aqua
        self._hp = [0, 0, 0, 100]#normal, fire, leaf, aqua

class EnemyFire(Enemy):
    def __init__(self):
        super().__init__()
        self._images = [pg.image.load(r"..\\images\\enemy_fire.png")] * 4  # 4枚同じ画像でリストを作る
        self._image = self._images[0]
        self._etype = "fire"
        self._maxhp = [0, 100, 0, 0]#normal, fire, leaf, aqua
        self._hp = [0, 100, 0, 0]#normal, fire, leaf, aqua

class BombEffect():
    def __init__(self, rect, effects):
        self._images = [
            pg.image.load(r"..\\images\\bomb_0.png"),
            pg.image.load(r"..\\images\\bomb_1.png"),
            pg.image.load(r"..\\images\\bomb_2.png"),
            pg.image.load(r"..\\images\\bomb_3.png"),
            pg.image.load(r"..\\images\\bomb_4.png"),
            pg.image.load(r"..\\images\\bomb_5.png")
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
        # Add more enemy types here as needed
        return None
    
    def random_create(self):
        etypes = random.choice(["leaf", "fire", "aqua"])
        return self.create(etypes)