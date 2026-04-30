import pygame as pg

class Observer():
    def update(self, ntype):
        pass

class Status(Observer):
    def __init__(self):
        self.reset()
        self._board = pg.Surface((800, 36), pg.SRCALPHA)

    @property
    def score(self):
        return self._score
            
    def reset(self):
        self._font = pg.font.Font(None, 32)
        self._distance = 0
        self._score = 0

    def update(self, ntype):
        if ntype == "distance":
            self._distance += 1
        elif ntype == "score":
            self._score += 100

    def draw(self, screen):
        #pg.draw.rect(self._board, (0,0,0,128), pg.Rect(0, 0, 320, 40))# (0,0,0,128)はRGB透明
        #screen.blit(self._board, (0, 0))
        info1 = self._font.render(f"Distance: {self._distance}", True, pg.Color("WHITE"))
        info2 = self._font.render(f"Score: {self._score}", True, pg.Color("WHITE"))
        screen.blit(info1, (10, 5))
        screen.blit(info2, (10, 25))
