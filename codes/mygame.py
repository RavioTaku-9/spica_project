import pygame as pg, sys
import gamecontrol, resultscene

pg.init()
screen_width, screen_height = 1600, 900
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("spica_proto")
game = gamecontrol.GameManager()
result = resultscene.ResultScene(game)

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
    pg.time.Clock().tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

