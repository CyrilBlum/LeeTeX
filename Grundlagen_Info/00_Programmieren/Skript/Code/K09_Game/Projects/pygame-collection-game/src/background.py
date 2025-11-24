import pygame as pg


class Background:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.sunset_color = (255, 204, 0)  # Color of the sunset
        self.sky_color = (100, 150, 255)  # Color of the sky
        self.sea_color = (20, 80, 160)  # Color of the sea
        self.sun_position = (screen_width // 2, screen_height // 3)
        self.sun_radius = 60

    def draw(self, screen):
        # Draw the sky
        for y in range(0, self.screen_height // 2):
            c = 100 + int(155 * (y / (self.screen_height // 2)))  # Gradient effect
            pg.draw.rect(screen, (c, 120, 180), (0, y, self.screen_width, 1))

        # Draw the sun
        pg.draw.circle(screen, self.sunset_color, self.sun_position, self.sun_radius)

        # Draw the sea
        pg.draw.rect(
            screen,
            self.sea_color,
            (0, self.screen_height // 2, self.screen_width, self.screen_height // 2),
        )

    def update(self):
        # Optional: Update the sun position for animation
        if self.sun_position[1] < self.screen_height // 2 + 100:
            self.sun_position = (
                self.sun_position[0],
                self.sun_position[1] + 1,
            )  # Move the sun down
