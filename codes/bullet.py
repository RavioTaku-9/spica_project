from config import SCREEN_WIDTH
from utils import Entity, load_image, is_off_screen


class Bullet(Entity):
    def __init__(self, rect):
        x = rect.x + 80
        y = rect.y + 20

        self._image = load_image("bullet.png")
        self._rect = self._image.get_rect()
        self._rect.topleft = (x, y)
        self._vx = 10
        self._vy = 0
        self._is_alive = True
        self._damage = [100, 34, 34, 34]  # normal, fire, leaf, aqua

    @property
    def damage(self):
        return self._damage

    def update(self):
        self._rect.x += self._vx
        self._rect.y += self._vy
        if self._rect.x > SCREEN_WIDTH:
            self._is_alive = False

    def draw(self, screen):
        screen.blit(self._image, self._rect)

class FireBullet(Bullet):
    def __init__(self, rect):
        super().__init__(rect)
        self._image = load_image("bullet_fire.png")
        self._damage = [34, 100, 0, 0]  # normal, fire, leaf, aqua

class LeafBullet(Bullet):
    def __init__(self, rect):
        super().__init__(rect)
        self._image = load_image("bullet_leaf.png")
        self._damage = [34, 0, 100, 0]  # normal, fire, leaf, aqua

class AquaBullet(Bullet):
    def __init__(self, rect):
        super().__init__(rect)
        self._image = load_image("bullet_aqua.png")
        self._damage = [34, 0, 0, 100]  # normal, fire, leaf, aqua

class EnemyBullet(Bullet):
    def __init__(self, rect,vx=-10, vy=0):
        super().__init__(rect)
        self._image = load_image("enemy_bullet.png")
        self._vx = vx
        self._vy = vy

    def update(self):
        self._rect.x += self._vx
        self._rect.y += self._vy
        # 画面外に出たら削除
        if is_off_screen(self._rect):
            self._is_alive = False
