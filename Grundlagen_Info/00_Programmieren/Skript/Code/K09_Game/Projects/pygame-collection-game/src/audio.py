import pygame as pg
from pathlib import Path

base_dir = Path(__file__).parent.parent
assets = base_dir / "assets" / "sounds"

class AudioManager:
    def __init__(self):
        pg.mixer.init()
        self.sounds = {}
        self.load_sounds()

    def load_sounds(self):
        self.sounds['item_collect'] = pg.mixer.Sound(str(assets / 'collect.mp3'))
        self.sounds['background_music'] = pg.mixer.Sound(str(assets / 'background_music.mp3'))

    def play_sound(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].play()

    def play_collect_sound(self):
        self.play_sound('item_collect')

    def play_background_music(self):
        self.sounds['background_music'].play(-1)  # Loop the background music

    def stop_background_music(self):
        self.sounds['background_music'].stop()