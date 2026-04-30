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
        self._status.reset()
        self._effects.clear()
        sound.SoundManager.get_instance().bgmstart()
        """
        for i in range(8):
            self._enemies.append(enemy.Enemy())
        """
    def update(self):
        self.notify("distance")
        self._background.update(1600)
        self._bullet_count += 1
        if self._bullet_count >= 4:
            key = pg.key.get_pressed()
            if key[pg.K_s]:
                b = bullet.Bullet(self._player.rect)
                self._bullets.append(b)
                self._bullet_count = 0
            if key[pg.K_r]:
                b = bullet.FireBullet(self._player.rect)
                self._bullets.append(b)
                self._bullet_count = 0
            if key[pg.K_a]:
                b = bullet.LeafBullet(self._player.rect)
                self._bullets.append(b)
                self._bullet_count = 0
            if key[pg.K_v]:
                b = bullet.AquaBullet(self._player.rect)
                self._bullets.append(b)
                self._bullet_count = 0

            
        for e in self._effects:
            e.update()
        for b in self._bullets:
            b.update()
        self._player.update()
        self._spawn_count += 1
        #敵の生成
        if self._spawn_count >= 40:
            self._enemies.append(self._factory.random_create())
            self._spawn_count = 0

        #remove_enemies = []
        #remove_bullets = []
        for e in self._enemies:
            for b in self._bullets:
                if e.rect.colliderect(b.rect):
                    #sound.SoundManager.get_instance().playattack()
                    #remove_bullets.append(b)

                    b.is_alive = False
                    if b.is_alive == False:
                        self._bullets.remove(b)
                    #e.hp -= 100
                    e.hp = [hp - dmg for hp, dmg in zip(e.hp, b.damage)]
                    #if e.hp <= 0:
                    if all(hp <= 0 for hp in e.hp):
                        self.notify("score")
                        self._effects.append(enemy.BombEffect(e.rect, self._effects))
                        sound.SoundManager.get_instance().playblast()
                        e.is_alive = False
                        #remove_enemies.append(e)
                        """
                        if len(self._enemies) == 0:
                            self._is_playing = False
                            self._is_cleared = True
                        """
            
            #敵が画面外に出たら消失
            #if e.rect.x <= -100:
            #    e.is_alive = False
            #    #remove_enemies.append(e)
            e.update()
            if e.is_alive == False:
                self._enemies.remove(e)
                break

            if e.rect.colliderect(self._player.rect):
                sound.SoundManager.get_instance().bgmstop()
                sound.SoundManager.get_instance().playover()
                self._is_playing = False
                self._is_cleared = False
            

        """
        for b in remove_bullets:
            if b in self._bullets:
                self._bullets.remove(b)
        for e in remove_enemies:
            if e in self._enemies:
                self._enemies.remove(e)
        
        if len(self._enemies) == 0:
            self._is_playing = False
            self._is_cleared = True
        """
        """
                if e.hp <= 0:
                    b = enemy.BombEffect(e.rect, self._effects)
                    self._effects.append(b)
                    self._enemies.remove(e)
                    if len(self._enemies) == 0:
                        self._is_playing = False
                        self._is_cleared = True
                    return
                """
    def draw(self, screen):
        self._background.draw(screen, 1600)
        for b in self._bullets:
            b.draw(screen)
        for e in self._effects:
            e.draw(screen)
        self._player.draw(screen)
        for e in self._enemies:
            e.draw(screen)
        self._status.draw(screen)