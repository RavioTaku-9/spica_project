from pathlib import Path

TITLE = "Spica"

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR.parent / "images"
SOUND_DIR = BASE_DIR.parent / "sounds"

TITLE_IMAGE = IMAGE_DIR / "background_night_town.png"
TITLEMSG_IMAGE = IMAGE_DIR / "title_transparent_2.png"
BACKGROUND_IMAGE = IMAGE_DIR / "background_night_town.png"
GAMECLEAR_IMAGE = IMAGE_DIR / "gameclear.png"
GAMEOVER_IMAGE = IMAGE_DIR / "gameover.png"

#基本となるサイズ
BASE_SCREEN_WIDTH = 160
BASE_SCREEN_HEIGHT = 144
CUT_HEIGHT = 125

#実際にモニターに映すサイズ
SCREEN_WIDTH = 160 * 4
SCREEN_HEIGHT = 144 * 4

RATIO_X = SCREEN_WIDTH / BASE_SCREEN_WIDTH
RATIO_Y = SCREEN_HEIGHT / BASE_SCREEN_HEIGHT

def scale_x(value):
    return int(value * RATIO_X)

def scale_y(value):
    return int(value * RATIO_Y)

SPICA_HP_MAX = 1
IFRAMES = 60
