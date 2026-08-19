import pygame as pg, sys
import gamecontrol, resultscene
import config

pg.init()

info = pg.display.Info()
config.SCREEN_WIDTH = min(config.SCREEN_WIDTH, info.current_w - 80)
config.SCREEN_HEIGHT = min(config.SCREEN_HEIGHT, info.current_h - 120)

screen = pg.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pg.RESIZABLE)
pg.display.set_caption(config.TITLE)

game = gamecontrol.GameManager()
result = resultscene.ResultScene(game)

while True:
    screen.fill(pg.Color("WHITE"))
    if game.is_playing == True:
        game.update()
        
    else:
        result.update()

    game.draw(screen)
    if game.is_playing == False:
        result.draw(screen)

    #pg.draw.rect(screen, pg.Color("WHITE"), pg.Rect(0, 130 * config.RATIO_Y, config.SCREEN_WIDTH, (config.BASE_SCREEN_HEIGHT - 120) * config.RATIO_Y))
    pg.display.update()
    pg.time.Clock().tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

