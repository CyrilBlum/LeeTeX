import pygame as pg


class Item:
    def __init__(self, x, y, width, height, points):
        self.rect = pg.Rect(x, y, width, height)
        self.points = points
        self.collected = False

    def draw(self, screen):
        if not self.collected:
            pg.draw.rect(screen, (255, 215, 0), self.rect)  # Gold color for the item

    def collect(self):
        self.collected = True
        self.rect.topleft = (-100, -100)  # Move off-screen or handle as needed
