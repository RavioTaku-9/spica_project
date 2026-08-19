import pygame as pg

from config import BACKGROUND_IMAGE, GAMECLEAR_IMAGE, GAMEOVER_IMAGE, RATIO_X, RATIO_Y, RATIO_Y, TITLE, TITLE_IMAGE, SCREEN_WIDTH, SCREEN_HEIGHT

class ResultScene():
    def __init__(self, game):
        font = pg.font.Font(None, int(50 * RATIO_X))
        self._game = game
        self._msg = font.render("Press SPACE to replay.", True, pg.Color("WHITE"))
        self._titlemsg = font.render(TITLE, True, pg.Color("WHITE"))

        self._gameover = pg.image.load(GAMEOVER_IMAGE).convert_alpha()
        w, h = self._gameover.get_size()
        self._gameover = pg.transform.smoothscale(self._gameover,(int(w * RATIO_X), int(h * RATIO_Y)))

        self._gameover_spica = pg.image.load(r"..\\images\\gameover_spica.PNG").convert_alpha()
        w, h = self._gameover_spica.get_size()
        self._gameover_spica = pg.transform.smoothscale(self._gameover_spica,(int(w * RATIO_X), int(h * RATIO_Y)))

        self._gameclear = pg.image.load(GAMECLEAR_IMAGE).convert_alpha()
        w, h = self._gameclear.get_size()
        self._gameclear = pg.transform.smoothscale(self._gameclear, (int(w * RATIO_X), int(h * RATIO_Y)))

        self._title = pg.image.load(TITLE_IMAGE).convert_alpha()    
        w, h = self._title.get_size()
        self._title = pg.transform.smoothscale(self._title, (int(w * RATIO_X), int(h * RATIO_Y)))

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_SPACE]:
            self._game.reset()

    def draw(self, screen):
        screen.blit(self._msg, (int(150 * RATIO_X), int(380 * RATIO_X)))
        if self._game._is_titling:
            screen.blit(self._title, (0, 0))
            screen.blit(self._titlemsg, (int(SCREEN_WIDTH*0.33 * RATIO_X), int(380 * RATIO_X)))
            screen.blit(self._msg, (int(SCREEN_WIDTH*0.3 * RATIO_X), int(SCREEN_HEIGHT*0.6 * RATIO_X)))
            
        elif self._game.is_playing == False:
            if self._game.is_cleared == True:
                screen.blit(self._gameclear, (int(150 * RATIO_X), int(200 * RATIO_X)))
                screen.blit(self._gameover_spica, (int(800 * RATIO_X), int(100 * RATIO_X)))
            else:
                screen.blit(self._gameover, (int(150 * RATIO_X), int(200 * RATIO_X)))
                screen.blit(self._gameover_spica, (int(800 * RATIO_X), int(100 * RATIO_X)))