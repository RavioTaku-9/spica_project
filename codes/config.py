from pathlib import Path

import pygame as pg

TITLE = "Spica: Starlight"

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR.parent / "images"
SOUND_DIR = BASE_DIR.parent / "sounds"

TITLE_IMAGE = IMAGE_DIR / "background_night.png"
BACKGROUND_IMAGE = IMAGE_DIR / "background_night.png"
GAMECLEAR_IMAGE = IMAGE_DIR / "gameclear.png"
GAMEOVER_IMAGE = IMAGE_DIR / "gameover.png"

SCREEN_WIDTH = 1600 # x方向の画面サイズ
SCREEN_HEIGHT = 900 # y方向の画面サイズ


def load_image(path):
    """Load an image, raising a clear error that identifies the failing file."""
    if not Path(path).exists():
        raise FileNotFoundError(f"Image asset not found: {path}")
    try:
        return pg.image.load(str(path))
    except pg.error as e:
        raise RuntimeError(f"Failed to load image {path}: {e}") from e


def load_sound(path):
    """Load a sound effect, raising a clear error that identifies the failing file."""
    if not Path(path).exists():
        raise FileNotFoundError(f"Sound asset not found: {path}")
    try:
        return pg.mixer.Sound(str(path))
    except pg.error as e:
        raise RuntimeError(f"Failed to load sound {path}: {e}") from e


def load_music(path):
    """Load a music track, raising a clear error that identifies the failing file."""
    if not Path(path).exists():
        raise FileNotFoundError(f"Music asset not found: {path}")
    try:
        pg.mixer.music.load(str(path))
    except pg.error as e:
        raise RuntimeError(f"Failed to load music {path}: {e}") from e






