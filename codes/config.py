from pathlib import Path

TITLE = "Starlit Spica Pocket"

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR.parent / "images"
SOUND_DIR = BASE_DIR.parent / "sounds"

#基本となるサイズ
BASE_SCREEN_WIDTH = 160
BASE_SCREEN_HEIGHT = 144
CUT_HEIGHT = 125

#実際にモニターに映すサイズ
SCREEN_WIDTH = 160 * 4
SCREEN_HEIGHT = 144 * 4

RATIO_X = SCREEN_WIDTH / BASE_SCREEN_WIDTH
RATIO_Y = SCREEN_HEIGHT / BASE_SCREEN_HEIGHT

SPICA_HP_MAX = 2
TIMEOUT = 60
