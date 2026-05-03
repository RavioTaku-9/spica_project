import pygame as pg
import player, enemy, bullet, background, status, sound

class Subject():
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)
        
    def notify(self, ntype):
        for observer in self._observers:
            observer.update(ntype)

class GameManager(Subject):
    def __init__(self):
        super().__init__()
        self._player = player.Player()
        self._enemies = []
        self._effects = []
        self._factory = enemy.EnemyFactory()
        self._status = status.Status()
        self.attach(self._status)
        self._bullets = []
        self._enemy_bullets = []
        self._enemy_fire_time = 0
        self._background = background.Background()
        self.reset()
        #起動時の設定
        self._is_titling = True
        self._is_playing = False
    
    @property
    def is_titling(self):
        return self._is_titling

    @property
    def is_playing(self):
        return self._is_playing
    @property
    def is_cleared(self):
        return self._is_cleared
    
    def reset(self):
        self._is_titling = False
        self._is_playing = True
        self._is_cleared = False
        self._player.reset()
        self._enemies.clear()
        self._spawn_count = 0
        self._bullets.clear()
        self._bullet_count = 0
        self._enemy_bullets.clear()
        self._enemy_fire_time = 0
        self._status.reset()
        self._effects.clear()
        sound.SoundManager.get_instance().stop_over()
        sound.SoundManager.get_instance().bgmstart()

    def update(self):
        self.notify("distance")
        self._background.update(1600)
        self._bullet_count += 1
        self._enemy_fire_time += 1

        if self._bullet_count >= 4:
            key = pg.key.get_pressed()
            if key[pg.K_s]:
                b = bullet.Bullet(self._player.rect)
                self._bullets.append(b)
                self._bullet_count = 0
            if key[pg.K_w]:
                b = bullet.FireBullet(self._player.rect)
                self._bullets.append(b)
                self._bullet_count = 0
            if key[pg.K_a]:
                b = bullet.LeafBullet(self._player.rect)
                self._bullets.append(b)
                self._bullet_count = 0
            if key[pg.K_x]:
                b = bullet.AquaBullet(self._player.rect)
                self._bullets.append(b)
                self._bullet_count = 0

        # 敵の弾の生成
        if self._enemy_fire_time >= 120:  # 2秒ごとに弾を発射
            for e in self._enemies:
                if e.is_alive:
                    self._enemy_bullets.append(bullet.EnemyBullet(e.rect, vx=-10, vy=-5)) 
                    self._enemy_bullets.append(bullet.EnemyBullet(e.rect, vx=-10, vy=0)) 
                    self._enemy_bullets.append(bullet.EnemyBullet(e.rect, vx=-10, vy=5)) 
            self._enemy_fire_time = 0

        for e in self._effects:
            e.update()
        for b in self._bullets:
            b.update()
        for b in self._enemy_bullets:
            b.update()
        # プレイヤーの弾削除処理を追加
        self._bullets = [b for b in self._bullets if b.is_alive] 
        # 敵の弾の削除処理
        self._enemy_bullets = [b for b in self._enemy_bullets if b.is_alive]
        self._player.update()
        self._spawn_count += 1
        #敵の生成
        if self._spawn_count >= 40:
            self._enemies.append(self._factory.random_create())
            self._spawn_count = 0

        for e in self._enemies:
            for b in self._bullets:
                if e.rect.colliderect(b.rect):
                    b.is_alive = False
                    e.hp = [hp - dmg for hp, dmg in zip(e.hp, b.damage)]
                    if all(hp <= 0 for hp in e.hp):
                        self.notify("score")
                        self._effects.append(enemy.BombEffect(e.rect, self._effects))
                        sound.SoundManager.get_instance().playblast()
                        e.is_alive = False

            e.update()
            #プレイヤーと敵の衝突判定
            if e.rect.colliderect(self._player.rect):
                sound.SoundManager.get_instance().bgmstop()
                sound.SoundManager.get_instance().playover()
                self._is_playing = False
                self._is_cleared = False
                
        self._enemies = [e for e in self._enemies if e.is_alive]

        #敵の弾とプレイヤーの衝突判定
        for b in self._enemy_bullets:
            if b.rect.colliderect(self._player.rect):
                sound.SoundManager.get_instance().bgmstop()
                sound.SoundManager.get_instance().playover()
                self._is_playing = False
                self._is_cleared = False
                
    def draw(self, screen):
        self._background.draw(screen, 1600)
        for b in self._bullets:
            b.draw(screen)
        for e in self._effects:
            e.draw(screen)
        self._player.draw(screen)
        for e in self._enemies:
            e.draw(screen)
        for b in self._enemy_bullets:
            b.draw(screen)

        self._status.draw(screen)