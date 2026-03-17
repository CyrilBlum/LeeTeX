import pygame as pg
import random
import math

# screen, colors
BG = (25, 30, 35)
FPS = 60

pg.init()

# Start in fullscreen. Using (0, 0) lets pygame pick the desktop size.
# On macOS, this produces a proper fullscreen surface.
flags = pg.FULLSCREEN
screen = pg.display.set_mode((0, 0), flags)
W, H = screen.get_size()
pg.display.set_caption("Tank Duel (Fullscreen)")

# Speed settings
speed_angle = 0.04
speed_tank = 6
speed_bullet = 30
gravity = 9.81 / FPS

# Game settings
target_points = 5

# Sounds
bg_sound = pg.mixer.Sound(
    "Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/tank_game.mp3"
)
shoot_sound = pg.mixer.Sound(
    "Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/shoot_bomb.mp3"
)
reload_sound = pg.mixer.Sound(
    "Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/reload.mp3"
)
moving_sound = pg.mixer.Sound(
    "Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/metal-moving.mp3"
)
explosion_sound = pg.mixer.Sound(
    "Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/explosion.mp3"
)
level_up_sound = pg.mixer.Sound(
    "Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/level_up.mp3"
)
heal_sound = pg.mixer.Sound(
    "Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/heal.mp3"
)


# Bilder
explosion_img = pg.image.load(
    "Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/explosion.png"
).convert_alpha()
explosion_img = pg.transform.scale(explosion_img, (80, 80))

heal_img = pg.image.load(
    "Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/firstaid.png"
).convert_alpha()
heal_img = pg.transform.scale(heal_img, (40, 40))

# Hintergrundmusik
bg_sound.play(loops=-1)
