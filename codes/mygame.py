import pygame as pg, sys
import gamecontrol, resultscene
from config import SCREEN_WIDTH, SCREEN_HEIGHT, TITLE

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption(TITLE)
game = gamecontrol.GameManager()
result = resultscene.ResultScene(game)

clock = pg.time.Clock()

try:
    while True:
        screen.fill(pg.Color("NAVY"))
        if game.is_playing == True:
            game.update()
        else:
            result.update()

        game.draw(screen)
        if game.is_playing == False:
            result.draw(screen)

        pg.display.update()
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
finally:
    pg.quit()

