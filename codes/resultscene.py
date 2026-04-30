import pygame as pg

class ResultScene():
    def __init__(self, game):
        font = pg.font.Font(None, 50)
        self._game = game
        self._msg = font.render("Press SPACE to replay.", True, pg.Color("WHITE"))
        self._titlemsg = font.render("WIZARD SPICA", True, pg.Color("WHITE"))
        self._gameover = pg.image.load(r"..\\images\\gameover.png")
        self._gameover_spica = pg.image.load(r"..\\images\\gameover_spica.PNG")
        self._gameclear = pg.image.load(r"..\\images\\gameclear.png")
        self._title = pg.image.load(r"..\\images\\background.jpg")

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_SPACE]:
            self._game.reset()

    def draw(self, screen):
        screen.blit(self._msg, (150, 380))
        if self._game._is_titling:
            screen.blit(self._title, (0, 0))
            screen.blit(self._titlemsg, (150, 380))
            screen.blit(self._msg, (150, 700))
        elif self._game.is_playing == False:
            if self._game.is_cleared == True:
                screen.blit(self._gameclear, (150, 200))
                screen.blit(self._gameover_spica, (800, 100))
            else:
                screen.blit(self._gameover, (150, 200))
                screen.blit(self._gameover_spica, (800, 100))