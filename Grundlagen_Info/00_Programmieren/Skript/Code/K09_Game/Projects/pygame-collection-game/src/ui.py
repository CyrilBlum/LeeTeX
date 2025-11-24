import pygame as pg


class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pg.font.Font(None, 36)

    def display_score(self, score):
        score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def display_time(self, remaining_time):
        time_text = self.font.render(f"Time: {remaining_time}", True, (255, 255, 255))
        self.screen.blit(time_text, (10, 50))

    def update_window_title(self, remaining_time):
        pg.display.set_caption(f"Collection Game - Time Left: {remaining_time}")
