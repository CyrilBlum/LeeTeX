import pygame as pg
import random
import math
from terrain import *
pg.init()
target_points=5
explosion_sound = pg.mixer.Sound("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/explosion.mp3")

class Tank:
    def __init__(self,x,color,dir, SCREENW, SCREENH):
        self.SCREENW = SCREENW
        self.SCREENH = SCREENH
        self.x = x
        self.time_hit = 0
        self.hitX = None
        self.hitY = None
        self.size = 20
        self.h = self.size
        self.w = self.size * 2
        self.vy = 0
        self.angle = random.random() * 2 - 1  # radians upward
        self.color = color
        self.dir = dir  # +1 facing right, -1 left
        self.life = 100
        # place on terrain
        self.ground = terrain_top_at(self.x + self.w/2, self.h)
        self.y = self.ground

    def move(self,dx):
        new_x = max(0, min(self.SCREENW - self.w, self.x + dx))
        # Terrain slope constraint
        old_top = terrain_top_at(self.x + self.w/2, self.h)
        new_top = terrain_top_at(new_x + self.w/2, self.h)
        if abs(new_top - old_top) > 35:  # too steep to climb
            return
        self.x = new_x
        self.ground = terrain_top_at(self.x + self.w/2, self.h)
        if self.vy == 0:  # stick to ground when not jumping/falling
            self.y = self.ground

    def change_angle(self,da):
        self.angle = max(-1.0, min(1.0, self.angle + da))

    def jump(self):
        if self.y >= self.ground and self.vy == 0:
            self.vy = -14

    def update(self):
        # update ground (terrain can change on restart)
        self.ground = terrain_top_at(self.x + self.w/2, self.h)
        if self.y < self.ground or self.vy < 0:
            self.vy += 0.6
            self.y += self.vy
            if self.y > self.ground:
                self.y = self.ground
                self.vy = 0
        else:
            # ensure we sit on ground if not jumping
            self.y = self.ground

    def barrel_tip(self):
        cx = self.x + self.w / 2
        top = self.y
        L = self.size * 1.5
        bx = cx + self.dir * math.cos(self.angle) * L
        by = top - math.sin(self.angle) * L
        return cx, top, bx, by

    def rect(self):
        return pg.Rect(self.x, self.y, self.w, self.h)
    
    def hitbox(self):
        return pg.Rect(self.x, self.y - self.w // 2, self.w, self.h + self.w // 2)
    
    def draw(self,surf):
        pg.draw.rect(surf, self.color, (self.x, self.y, self.w, self.h))
        cx = self.x + self.w // 2
        cy = self.y + self.h // 2
        pg.draw.circle(surf, self.color, (cx, self.y), self.w // 2)
        pg.draw.rect(surf, BG, (self.x, cy, self.w, self.w // 2))
        cx, top, bx, by = self.barrel_tip()
        pg.draw.line(surf, self.color, (cx, top), (bx, by), 6)
        bar_w = self.w
        bar_h = 8
        life_ratio = self.life / 100
        pg.draw.rect(surf, (200,0,0), (self.x, self.y + self.h * .7, bar_w, bar_h))
        pg.draw.rect(surf, (0,200,0), (self.x, self.y + self.h * .7, bar_w * life_ratio, bar_h))

    def has_been_hit(self, hitX, hitY):
        explosion_sound.play()
        self.life -= 100 / target_points
        self.time_hit = 60
        self.hitX = hitX
        self.hitY = hitY