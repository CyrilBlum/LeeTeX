from terrain import *
from settings import *

bullets=[]


class Tank:
    def __init__(self,x,color,dir, SCREENW, SCREENH):
        self.SCREENW = SCREENW
        self.SCREENH = SCREENH
        self.x = x
        self.time_hit = 0
        self.hitX = None
        self.hitY = None
        self.size = 20
        # height, width
        self.height = self.size
        self.width = self.size * 2

        self.surface = pg.Surface((W, H), pg.SRCALPHA)
        self.centerx = self.x + self.width / 2

        self.speed_y = 0
        self.angle = random.random() * 2 - 1  # radians upward (-1 to +1), for the barrel
        self.color = color # RGB tuple
        self.dir = dir  # +1 facing right, -1 left, for barrel direction
        self.life = 100
        # place on terrain
        self.ground = terrain_top_at(self.x + self.width/2, self.height)
        self.y = self.ground

    def update_coordinates(self):
        self.centerx = self.x + self.width / 2

    def move(self,dx):
        new_x = max(0, min(self.SCREENW - self.width, self.x + dx))
        # Terrain slope constraint
        old_top = terrain_top_at(self.x + self.width/2, self.height)
        new_top = terrain_top_at(new_x + self.width/2, self.height)
        if abs(new_top - old_top) > 35:  # too steep to climb
            return
        self.x = new_x
        
        self.ground = terrain_top_at(self.x + self.width/2, self.height)
        if self.speed_y == 0:  # stick to ground when not jumping/falling
            self.y = self.ground

    def change_angle(self,da):
        self.angle = max(-1.0, min(1.0, self.angle + da))

    def jump(self):
        if self.y >= self.ground and self.speed_y == 0:
            self.speed_y = -14

    def update(self):
        # update ground (terrain can change on restart)
        self.ground = terrain_top_at(self.x + self.width/2, self.height)
        if self.y < self.ground or self.speed_y < 0:
            self.speed_y += 0.6
            self.y += self.speed_y
            if self.y > self.ground:
                self.y = self.ground
                self.speed_y = 0
        else:
            # ensure we sit on ground if not jumping
            self.y = self.ground

    def barrel_tip(self):
        L = self.size * 1.5

        bottom_barrel_x = self.x + self.width / 2
        bottom_barrel_y = self.y
        tip_barrel_x = bottom_barrel_x + self.dir * math.cos(self.angle) * L
        tip_barrel_y = bottom_barrel_y - math.sin(self.angle) * L
        return bottom_barrel_x, bottom_barrel_y, tip_barrel_x, tip_barrel_y

    def rect(self):
        return pg.Rect(self.x, self.y, self.width, self.height)
    
    def hitbox(self):
        return pg.Rect(self.x, self.y - self.width // 2, self.width, self.height + self.width // 2)
    
    def draw(self,surf):
        self.surface.fill((255,255,255,0))                         # notice the alpha value in the color
        # draw body
        pg.draw.rect(self.surface, self.color, (self.x, self.y, self.width, self.height))
        center_x = self.x + self.width // 2
        cy = self.y + self.height // 2
        pg.draw.circle(self.surface, self.color, (center_x, self.y), self.width // 2)
        pg.draw.rect(self.surface, BG, (self.x, cy, self.width, self.width // 2))
        # draw barrel
        center_x, top, bx, by = self.barrel_tip()
        pg.draw.line(self.surface, self.color, (center_x, top), (bx, by), 6)
        
        # draw life bar
        bar_w = self.width
        bar_h = 8
        life_ratio = self.life / 100
        pg.draw.rect(self.surface, (200,0,0), (self.x, self.y + self.height * .7, bar_w, bar_h))
        pg.draw.rect(self.surface, (0,200,0), (self.x, self.y + self.height * .7, bar_w * life_ratio, bar_h))

        #surf.blit(self.surface, (0,0))

    def has_been_hit(self, hitX, hitY):
        explosion_sound.play()
        self.life -= 100 / target_points
        self.time_hit = 60
        self.hitX = hitX
        self.hitY = hitY
        self.surface.set_alpha(int(self.life / 100 * 255))
        if self.life == 0:
            level_up_sound.play()


class Bullet:
    def __init__(self,x,y,vx,vy,owner):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.r=6
        self.owner=owner
    def update(self):
        self.x+=self.vx
        self.y += self.vy 
        self.vy += gravity  # gravity effect
    def outofscreen(self):
        return self.x<0 or self.x>W or self.y<0 or self.y>H
    def draw(self,surf):
        pg.draw.circle(surf,(250,240,200),(int(self.x),int(self.y)),self.r)
    def rect(self):
        return pg.Rect(self.x-self.r,self.y-self.r,self.r*2,self.r*2)

def fire(tank):
    center_x,top,bx,by = tank.barrel_tip()
    vx = (bx-center_x)/60*speed_bullet
    vy = (by-top)/60*speed_bullet
    bullets.append(Bullet(bx,by,vx,vy,tank))