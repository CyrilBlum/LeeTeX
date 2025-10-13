import pygame as pg
from settings import *
from random import randint
from player import Player
from item import Item
from background import Background
from ui import UI
from audio import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Collection Game")
        self.clock = pg.time.Clock()
        self.running = True
        self.player = Player(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT), 10, 30, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.items = [Item(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT), 30, 30, 10) for _ in range(NUM_ITEMS)]
        self.background = Background(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.ui = UI(self.screen)
        self.audio = AudioManager()
        self.start_time = pg.time.get_ticks()
        self.score = 0

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        # Move and update player (no drawing here)
        keys = pg.key.get_pressed()
        self.player.move(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.player.update()
        # Collisions
        for item in self.items:
            if self.player.rect.colliderect(item.rect):
                self.score += item.points
                # Adjust method name if your AudioManager differs
                item.collect()
                try:
                    self.audio.play_collect_sound()
                except Exception:
                    pass
        self.update_time()

    def update_time(self):
        elapsed_time = (pg.time.get_ticks() - self.start_time) / 1000
        remaining_time = max(0, 60 - elapsed_time)
        pg.display.set_caption(f"Collection Game - Score: {self.score} - Time Left: {int(remaining_time)}s")
        if remaining_time <= 0:
            self.running = False

    def render(self):
        self.background.draw(self.screen)
        self.player.draw(self.screen)  # draw after background so it stays visible
        for item in self.items:
            item.draw(self.screen)
        pg.display.flip()

    def quit(self):
        pg.quit()