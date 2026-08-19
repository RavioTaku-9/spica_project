import pygame as pg

from config import RATIO_X, RATIO_Y, SCREEN_WIDTH, SCREEN_HEIGHT

class Observer():
    def update(self, ntype):
        pass

class Status(Observer):
    def __init__(self):
        self.reset()
        self._board = pg.Surface((800 * RATIO_X, 10 * RATIO_Y), pg.SRCALPHA)

    @property
    def score(self):
        return self._score
            
    def reset(self):
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
        info2 = self._font.render(f"Score: {self._score}", True, pg.Color("BLACK"))
        info1 = self._font.render(f"Distance: {self._distance}", True, pg.Color("BLACK"))
        screen.blit(info2, (5 * RATIO_X, 128 * RATIO_Y))
        screen.blit(info1, (5 * RATIO_X, 136 * RATIO_Y))
        
