import pygame as pg

from config import IMAGE_DIR, SOUND_DIR, SCREEN_WIDTH, SCREEN_HEIGHT


def load_image(name):
    """Load an image from the shared images directory."""
    return pg.image.load(str(IMAGE_DIR / name))


def load_sound(name):
    """Load a sound effect from the shared sounds directory."""
    return pg.mixer.Sound(str(SOUND_DIR / name))


def load_music(name):
    """Load a background music track from the shared sounds directory."""
    pg.mixer.music.load(str(SOUND_DIR / name))


def advance_animation(images, cnt, rate=10):
    """Pick the current animation frame from a counter value."""
    return images[cnt // rate % len(images)]


def is_off_screen(rect, margin=100, width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
    """Return True when rect has moved fully outside the play area."""
    return (rect.x < -margin or rect.x > width + margin or
            rect.y < -margin or rect.y > height + margin)


class Entity:
    """Shared rect / alive state used by movable game objects."""

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value

    @property
    def is_alive(self):
        return self._is_alive

    @is_alive.setter
    def is_alive(self, value):
        self._is_alive = value
