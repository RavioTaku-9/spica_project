import pygame as pg

from config import RATIO_X, RATIO_Y, SCREEN_WIDTH, SCREEN_HEIGHT, SPICA_HP_MAX
import gamecontrol

class Observer():
    def update(self, ntype):
        pass

class Status(Observer):
    def __init__(self, game):
        self._game = game



        self.reset()
        self._board = pg.Surface((800 * RATIO_X, 10 * RATIO_Y), pg.SRCALPHA)

    @property
    def score(self):
        return self._score
            
    def reset(self):
        self._base_size = 8 * RATIO_X 
        self._w = self._base_size
        self._h = self._base_size
        self._spica_hp_images = [
            pg.transform.smoothscale(pg.image.load(r"..\\images\\spica_hp_0_16.png").convert_alpha(), (self._w, self._h)),
            pg.transform.smoothscale(pg.image.load(r"..\\images\\spica_hp_1_16.png").convert_alpha(), (self._w, self._h))
        ]
        self._spica_hp_image = self._spica_hp_images[0]
        self._font = pg.font.Font(None, int(10 * RATIO_X))
        self._distance = 0
        self._score = 0

    def update(self, ntype):
        if ntype == "distance":
            self._distance += 1
        elif ntype == "score":
            self._score += 100

    def draw(self, screen):
        #pg.draw.rect(self._board, (0,0,0,128), pg.Rect(0, 0, 320, 40)) #(0,0,0,128)はRGB透明
        #screen.blit(self._board, (0, 0))
        info1 = self._font.render(f"Score: {self._score}", True, pg.Color("BLACK"))
        info2 = self._font.render(f"Spica:", True, pg.Color("BLACK"))
        for i in range(SPICA_HP_MAX):
            screen.blit(self._spica_hp_images[0], (30 * RATIO_X + i * 10 * RATIO_X, 135 * RATIO_Y))
        for i in range(self._game.spica_hp):
            screen.blit(self._spica_hp_images[1], (30 * RATIO_X + i * 10 * RATIO_X, 135 * RATIO_Y))
        screen.blit(info1, (5 * RATIO_X, 128 * RATIO_Y))
        screen.blit(info2, (5 * RATIO_X, 136 * RATIO_Y))
        
