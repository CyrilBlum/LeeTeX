import pygame as pg
import random
import math

# screen, colors
BG = (25, 30, 35)
W, H = 900, 500
FPS = 60

pg.init()
screen = pg.display.set_mode((W, H))
pg.display.set_caption("Tank Duel")

# Speed settings
speed_angle = 0.04
speed_tank = 6
speed_bullet = 15
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


# Bilder
explosion_img = pg.image.load(
    "Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/explosion.png"
).convert_alpha()
explosion_img = pg.transform.scale(explosion_img, (80, 80))

# Hintergrundmusik
bg_sound.play(loops=-1)
