import pygame as pg

from config import BACKGROUND_IMAGE, GAMECLEAR_IMAGE, GAMEOVER_IMAGE, TITLE, TITLE_IMAGE, SCREEN_WIDTH, SCREEN_HEIGHT

class ResultScene():
    def __init__(self, game):
        font = pg.font.Font(None, 50)
        self._game = game
        self._msg = font.render("Press SPACE to replay.", True, pg.Color("WHITE"))
        self._titlemsg = font.render(TITLE, True, pg.Color("WHITE"))
        self._gameover = pg.image.load(GAMEOVER_IMAGE)
        self._gameover_spica = pg.image.load(r"..\\images\\gameover_spica.PNG")
        self._gameclear = pg.image.load(GAMECLEAR_IMAGE)
        self._title = pg.image.load(TITLE_IMAGE)

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_SPACE]:
            self._game.reset()

    def draw(self, screen):
        screen.blit(self._msg, (150, 380))
        if self._game._is_titling:
            screen.blit(self._title, (0, 0))
            screen.blit(self._titlemsg, (SCREEN_WIDTH*0.33, 380))
            screen.blit(self._msg, (SCREEN_WIDTH*0.3, SCREEN_HEIGHT*0.6))
            
        elif self._game.is_playing == False:
            if self._game.is_cleared == True:
                screen.blit(self._gameclear, (150, 200))
                screen.blit(self._gameover_spica, (800, 100))
            else:
                screen.blit(self._gameover, (150, 200))
                screen.blit(self._gameover_spica, (800, 100))