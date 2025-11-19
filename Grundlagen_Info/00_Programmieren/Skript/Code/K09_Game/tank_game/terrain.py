import random
import pygame as pg
from settings import *

# Terrain globals
terrain_heights = []  # raw elevation values
terrain_surface = []  # y pixel positions of surface
TERRAIN_BASELINE = H - 140  # average vertical position of terrain surface
TERRAIN_AMPLITUDE = 250
TERRAIN_COLOR = (45,50,55)




def generate_fbm_terrain(width, baseline, amplitude, octaves=5, persistence=0.5, lacunarity=2.0):
    """Generate a 1D fractal Brownian motion terrain profile.
    Returns list of surface y pixel positions length=width.
    Higher value means lower on screen (because y grows downward)."""
    heights = [0.0] * width
    for o in range(octaves):
        freq = lacunarity ** o
        n_points = int(freq) + 2
        control = [random.random() for _ in range(n_points)]
        scale_x = (width - 1) / (n_points - 1)
        octave_amp = amplitude * (persistence ** o)
        for x in range(width):
            idx = x / scale_x
            i0 = int(idx)
            i1 = min(i0 + 1, n_points - 1)
            t = idx - i0
            v = (1 - t) * control[i0] + t * control[i1]
            heights[x] += v * octave_amp
    # Normalize heights so that mean ~ 0
    mean_h = sum(heights) / width
    for x in range(width):
        heights[x] -= mean_h
    surface = [int(baseline + h) for h in heights]
    # Clamp to screen
    for x in range(width):
        surface[x] = max(50, min(H - 50, surface[x]))
    return heights, surface

def init_terrain():
    global terrain_heights, terrain_surface
    terrain_heights, terrain_surface = generate_fbm_terrain(W, TERRAIN_BASELINE, TERRAIN_AMPLITUDE)

def draw_terrain(surf):
    if not terrain_surface:
        return
    # Build polygon from left to right
    poly = [(0, H)]
    for x in range(W):
        poly.append((x, terrain_surface[x]))
    poly.append((W, H))
    pg.draw.polygon(surf, TERRAIN_COLOR, poly)
    # Slight highlight ridge
    ridge_color = (70,75,80)
    for x in range(0, W, 3):
        pg.draw.line(surf, ridge_color, (x, terrain_surface[x]-2), (x, terrain_surface[x]+2), 1)

def terrain_top_at(x, obj_height):
    """Return the y coordinate for the top of an object of height obj_height resting on terrain at horizontal x (center)."""
    cx = int(max(0, min(W - 1, x)))
    surface_y = terrain_surface[int(cx)] if terrain_surface else (H - 60)
    return surface_y - obj_height

def terrain_surface_y(x):
    cx = int(max(0, min(W - 1, x)))
    return terrain_surface[cx] if terrain_surface else (H - 60)