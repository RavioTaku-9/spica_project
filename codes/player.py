import pygame as pg
from config import CUT_HEIGHT,  RATIO_X, RATIO_Y, SCREEN_HEIGHT, SCREEN_WIDTH, IMAGE_DIR, TIMEOUT

class PlayerState():
    def __init__(self, player):
        self._player = player
        self._image = None
        self._is_visible = True
        self._base_size = 16 * RATIO_X  # 基本サイズをRATIO_Xでスケーリング。16とはピクセル数
        self._w = self._base_size
        self._h = self._base_size
        
    
    def update(self):
        pass
    
    def draw(self, screen, rect):
        screen.blit(self._image, rect)
    
    @property
    def image(self):
        return self._image
    
class StartState(PlayerState):
    def __init__(self, player):
        super().__init__(player)
        self._images = [
                    pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "bomb_star_2_16.png").convert_alpha(), (self._w, self._h)),
                    pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "bomb_star_3_16.png").convert_alpha(), (self._w, self._h)),
                    pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "bomb_star_4_16.png").convert_alpha(), (self._w, self._h)),
                    pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "bomb_star_5_16.png").convert_alpha(), (self._w, self._h)),
                ]
        self._image = self._images[0]
        self._cnt = 0
        self._is_visible = True
        
    def update(self):
        self._cnt += 1
        self._image = self._images[self._cnt // 10 % 4]
        if self._cnt >= 20:
            return IdleState(self._player)
        return self
    

class IdleState(PlayerState):
    def __init__(self, player):
        super().__init__(player)
        self._images = [
                    pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "majo_side_1_100.png").convert_alpha(), (self._w, self._h)),
                    pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "majo_side_2_100.png").convert_alpha(), (self._w, self._h)),
                    pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "majo_side_1_100.png").convert_alpha(), (self._w, self._h)),
                    pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "majo_side_2_100.png").convert_alpha(), (self._w, self._h)),
                ]
        self._image = self._images[0]
        self._cnt = 0
        self._is_visible = True

    def update(self):
        self._cnt += 1
        self._image = self._images[self._cnt // 10 % 4]
        key = pg.key.get_pressed()
        if key[pg.K_LEFT] or key[pg.K_RIGHT] or key[pg.K_UP] or key[pg.K_DOWN]:
            return MovingState(self._player)
        else:
            return self

class MovingState(PlayerState):
    def __init__(self, player):
        super().__init__(player)
        self._images = [
                    pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "majo_side_1_100.png").convert_alpha(), (self._w, self._h)),
                    pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "majo_side_2_100.png").convert_alpha(), (self._w, self._h)),
                    pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "majo_side_1_100.png").convert_alpha(), (self._w, self._h)),
                    pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "majo_side_2_100.png").convert_alpha(), (self._w, self._h)),
                ]
        self._image = self._images[0]
        self._cnt = 0
        self._is_visible = True
        
    def update(self):
        self._cnt += 1
        self._image = self._images[self._cnt // 10 % 4]
        key = pg.key.get_pressed()
        if not (key[pg.K_LEFT] or key[pg.K_RIGHT] or key[pg.K_UP] or key[pg.K_DOWN]):
            return IdleState(self._player)
        else:
            return self

class DamageState(PlayerState):
    def __init__(self, player):
        super().__init__(player)
        
        self._image = pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "majo_side_1_100.png").convert_alpha(), (self._w, self._h))
        self._cnt= 0
        self._is_visible = True

    def update(self):
        self._cnt += 1
        if self._player._timeout <= 0:
            return IdleState(self._player)
        else:
            return self
        
    def draw(self, screen, rect):
        # 点滅ロジックをここに移動
        if self._cnt % 6 < 3:
            return  # 描画しない
        else:
            screen.blit(self._image, rect)
            
class GameoverState(PlayerState):   #is_paying = false時の描画が難のため、ゲームオーバー時のアニメーションはgamecontrolで管理する。
    def __init__(self, player):
        super().__init__(player)
        self._is_visible = False  # 非表示にする
        
    def update(self):
        return self  # 常にGameOverStateのまま    

    def draw(self, screen, rect):
        pass  # 描画しない
        
class Player():
    def __init__(self):
        self._is_visible = True
        self._timeout = 0  # 追加
        self.reset()

    @property
    def rect(self):
        return self._rect
    @rect.setter
    def rect(self, value):
        self._rect = value

    def reset(self):
        self._is_visible = True
        self._base_size = 16 * RATIO_X  # 基本サイズをRATIO_Xでスケーリング。16とはピクセル数
        self._w = self._base_size
        self._h = self._base_size
        self._timeout = 0     
        self._state = StartState(self)
        self._rect = pg.Rect(SCREEN_WIDTH / 20, SCREEN_HEIGHT /2.5, self._w, self._h)
        self._speed = 1 * RATIO_X
        self._cnt = 0

    def update(self):
        self._state = self._state.update()

        #無敵時間がまだあればカウントを減らす
        if self._timeout > 0:
            self._timeout -= 1
            
        # StartStateのときは移動しない
        if isinstance(self._state, StartState):
            return
            
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
        # self._image = self._images[self._cnt // 10 % 4]

    def draw(self, screen):
        self._state.draw(screen, self._rect)
        
        # プレイヤーの近くに表示する弾の見本
        # fire_rect = self._rect.copy()
        # fire_rect.x += 3 * RATIO_X  
        # fire_rect.y -= 3 * RATIO_Y  
        #screen.blit(self._image_fire, fire_rect)
        # leaf_rect = self._rect.copy()
        # leaf_rect.x -= 3 * RATIO_X
        # leaf_rect.y += 3 * RATIO_Y  
        #screen.blit(self._image_leaf, leaf_rect)
        # aqua_rect = self._rect.copy()
        # aqua_rect.x += 3 * RATIO_X
        # aqua_rect.y += 11 * RATIO_Y
        #screen.blit(self._image_aqua, aqua_rect)

    def damage(self):
        self._state = DamageState(self)
        self._timeout = TIMEOUT  # ダメージ時にセット

    #無敵の有無を返す
    @property
    def is_invincible(self):
        return self._timeout > 0
    
    def die(self):
        self._state = GameoverState(self)  # クラス名に注意
        self._timeout = 0  # 無敵時間もリセット