import pygame as pg
import random
from config import load_sound, load_music

class SoundManager():
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        load_music(r"..//sounds//maou_bgm_piano40.mp3")
        self._start = load_sound(r"..//sounds//鈴を鳴らす.mp3")
        self._over_sounds = [
            load_sound(r"..//sounds//shozyo2-shobon.mp3"),
            load_sound(r"..//sounds//shozyo2-human.mp3"),
            #load_sound(r"..//sounds//shozyo1-yararema.mp3"),
        ]
        self._current_over = None  # 今鳴っている音を保持

        self._clear = load_sound(r"..//sounds//clear.wav")
        self._clap1 = load_sound(r"..//sounds//clap1.wav")
        self._clap2 = load_sound(r"..//sounds//clap2.wav")
        self._clap3 = load_sound(r"..//sounds//clap3.wav")
        
        self._bomb = load_sound(r"..//sounds//bomb.wav")
        self._blast = load_sound(r"..//sounds//blast.wav")
        self._blast1 = load_sound(r"..//sounds//Glocken01-1(Single).mp3")
        self._blast2 = load_sound(r"..//sounds//Glocken01-2(Single).mp3")
        self._blast3 = load_sound(r"..//sounds//Glocken01-3(Single).mp3")

    def bgmstart(self):
        pg.mixer.music.play(-1)

    def bgmstop(self):
        pg.mixer.music.stop()
    
    def playover(self):
        self._current_over = random.choice(self._over_sounds)
        self._current_over.play()

    def stop_over(self):
        if self._current_over:
            self._current_over.stop()
            self._current_over = None

    def playclear(self):
        self._clear.play()
    
    def playattack(self):
        r = random.randint(0, 3)
        if r == 0:
            self._clap1.play()
        elif r == 1:
            self._clap2.play()
        else:
            self._clap3.play()
    
    def playblast(self):
        #self._blast.play()
        r = random.randint(0, 3)
        if r == 0:
            self._blast1.play()
        elif r == 1:
            self._blast2.play()
        else:
            self._blast3.play()

    def playbomb(self):
        self._bomb.play()