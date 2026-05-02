import pygame as pg
class Bullet():
    def __init__(self, rect):
        x = rect.x + 80
        y = rect.y + 20

        self._image = pg.image.load(r"..\\images\\bullet.png")
        self._rect = self._image.get_rect()
        self._rect.topleft = (x, y)
        self._vx = 10
        self._is_alive = True
        self._damage = [100, 34, 34, 34]  # normal, fire, leaf, aqua

    @property
    def rect(self):
        return self._rect
    
    @property
    def damage(self):
        return self._damage

    def update(self):
        self._rect.x += self._vx
        if self._rect.x > 1600:
            self._is_alive = False

    def draw(self, screen):
        screen.blit(self._image, self._rect)

class FireBullet(Bullet):
    def __init__(self, rect):
        super().__init__(rect)
        self._image = pg.image.load(r"..\\images\\bullet_fire.png")
        self._damage = [34, 100, 0, 0]  # normal, fire, leaf, aqua

class LeafBullet(Bullet):
    def __init__(self, rect):
        super().__init__(rect)
        self._image = pg.image.load(r"..\\images\\bullet_leaf.png")
        self._damage = [34, 0, 100, 0]  # normal, fire, leaf, aqua

class AquaBullet(Bullet):
    def __init__(self, rect):
        super().__init__(rect)
        self._image = pg.image.load(r"..\\images\\bullet_aqua.png")
        self._damage = [34, 0, 0, 100]  # normal, fire, leaf, aqua