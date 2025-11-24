import pygame as pg


class Player:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.rect = pg.Rect(x, y, width, height)
        self.speed = 5
        self.score = 0
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move(self, keys, screen_width, screen_height):
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed

    def update(self):
        # Keep the player within the screen bounds (no drawing here)
        self.rect.clamp_ip(pg.Rect(0, 0, self.screen_width, self.screen_height))

    def draw(self, screen):
        pg.draw.rect(screen, (255, 255, 255), self.rect)

    def reset(self, x, y):
        self.rect.topleft = (x, y)
        self.score = 0

    def get_score(self):
        return self.score
