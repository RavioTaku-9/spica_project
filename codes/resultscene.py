import math

import pygame as pg
import player
import background
from config import IMAGE_DIR, RATIO_X, RATIO_Y, RATIO_Y, SCREEN_WIDTH, SCREEN_HEIGHT, BASE_SCREEN_WIDTH, BASE_SCREEN_HEIGHT

class ResultScene():
    def __init__(self, game):
        self._player_title = player.Player()
        self._background_title = background.Background()
        font = pg.font.Font(None, int(10 * RATIO_X))
        self._game = game

        self._title = pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "background_night_town.png").convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self._titlemsg = pg.transform.smoothscale(pg.image.load(IMAGE_DIR / "title_transparent_3.png").convert_alpha(), (SCREEN_WIDTH*0.8, SCREEN_HEIGHT*0.8))
        
        self._msg = font.render("Press SPACE to replay.", True, pg.Color("WHITE"))
        
        self._gameover = pg.image.load(IMAGE_DIR / "gameover.png").convert_alpha()
        w, h = self._gameover.get_size()
        self._gameover = pg.transform.smoothscale(self._gameover,(int(w * RATIO_X), int(h * RATIO_Y)))

        # self._gameover_spica = pg.image.load(r"..\\images\\gameover_spica.PNG").convert_alpha()
        # w, h = self._gameover_spica.get_size()
        # self._gameover_spica = pg.transform.smoothscale(self._gameover_spica,(int(w * RATIO_X), int(h * RATIO_Y)))

        self._gameclear = pg.image.load(IMAGE_DIR / "gameclear.png").convert_alpha()
        w, h = self._gameclear.get_size()
        self._gameclear = pg.transform.smoothscale(self._gameclear, (int(w * RATIO_X), int(h * RATIO_Y)))

    def update(self):
        if self._game._is_titling:
            # player_titleの処理
            if not hasattr(self, '_time'):
                self._time = 0
            self._time += 0.05
            # yはsin波で上下に揺らす（初期位置 + 振幅 * sin(時間)）
            amplitude = 10 * RATIO_Y  # 振幅
            base_y = SCREEN_HEIGHT / 1.7  # 基準位置
            self._player_title.rect.x = SCREEN_WIDTH / 2 - self._player_title.rect.width / 2
            self._player_title.rect.y = base_y + amplitude * math.sin(self._time)
            # 背景の処理
            self._background_title.update(SCREEN_WIDTH)
        
        key = pg.key.get_pressed()
        if key[pg.K_SPACE]:
            self._game.reset()

    def draw(self, screen):
        if self._game._is_titling:
            self._background_title.draw(screen, SCREEN_WIDTH)
            # screen.blit(self._title, (0, 0))
            screen.blit(self._titlemsg, (SCREEN_WIDTH/2 *0.2, SCREEN_HEIGHT/500-100))
            self._player_title.draw(screen)
            
            
        elif self._game.is_playing == False:
            if self._game.is_cleared == True:
                screen.blit(self._gameclear, (SCREEN_WIDTH/2 *0.5, SCREEN_HEIGHT/2))
                # screen.blit(self._gameover_spica, (int(800 * RATIO_X), int(100 * RATIO_X)))
            else:
                # screen.blit(self._gameover, (BASE_SCREEN_WIDTH/2 * RATIO_X, BASE_SCREEN_HEIGHT/2 * RATIO_Y))
                screen.blit(self._msg, (SCREEN_WIDTH/2 *0.5, SCREEN_HEIGHT/2))
                # screen.blit(self._gameover_spica, (int(800 * RATIO_X), int(100 * RATIO_X)))
