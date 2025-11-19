
from tank import Tank
from terrain import *
from datetime import datetime

pg.init()
W,H = 900,500
screen = pg.display.set_mode((W,H))
pg.display.set_caption("Tank Duel")
BG = (25,30,35)
FPS = 60
gravity = 9.81 / FPS
speed_angle = 0.04
speed_tank = 6
target_points=5
font = pg.font.Font(None,24)
clock = pg.time.Clock()
speed_bullet = 15
bullets=[]
score=[0,0]
running=True
winner=None
show_help=False

init_terrain()

# Sounds
bg_sound = pg.mixer.Sound("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/tank_game.mp3")
shoot_sound = pg.mixer.Sound("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/shoot_bomb.mp3")
reload_sound = pg.mixer.Sound("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/reload.mp3")

# Bilder
explosion_img = pg.image.load("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/explosion.png").convert_alpha()
explosion_img = pg.transform.scale(explosion_img,(80,80))

# Hintergrundmusik
bg_sound.play(loops=-1)

t1 = Tank(70,(120,200,90),1, W, H)
t2 = Tank(W-70-80,(200,90,90),-1, W, H)

class Bullet:
    def __init__(self,x,y,vx,vy,owner):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.r=6
        self.o=owner
    def update(self):
        self.x+=self.vx
        self.y += self.vy 
        self.vy += gravity  # gravity effect
    def off(self):
        return self.x<0 or self.x>W or self.y<0 or self.y>H
    def draw(self,surf):
        pg.draw.circle(surf,(250,240,200),(int(self.x),int(self.y)),self.r)
    def rect(self):
        return pg.Rect(self.x-self.r,self.y-self.r,self.r*2,self.r*2)

def fire(tank):
    cx,top,bx,by = tank.barrel_tip()
    vx = (bx-cx)/60*speed_bullet
    vy = (by-top)/60*speed_bullet
    bullets.append(Bullet(bx,by,vx,vy,tank))

while running:
    for e in pg.event.get():
        if e.type==pg.QUIT: 
            running=False
        elif e.type==pg.KEYDOWN:
            if e.key==pg.K_ESCAPE: 
                running=False
            # Toggle help overlay with Ctrl+K
            if (e.key == pg.K_k) and (e.mod & pg.KMOD_CTRL):
                show_help = not show_help
            if winner is None and e.key==pg.K_r:
                print("No winner yet")
            if winner is not None and e.key==pg.K_r:
                print("Restarting game")
                score=[0,0]
                bullets.clear()
                winner=None
                init_terrain()
                t1.x=70; t2.x=W-70-80
                t1.angle=0.3; t2.angle=0.3
                t1.life=100; t2.life=100
                # reposition tanks on new terrain
                t1.ground = terrain_top_at(t1.x + t1.width/2, t1.height); t1.y = t1.ground; t1.speed_y = 0
                t2.ground = terrain_top_at(t2.x + t2.width/2, t2.height); t2.y = t2.ground; t2.speed_y = 0
                reload_sound.play()
            if winner is None:
                if e.key==pg.K_SPACE: 
                    fire(t1)
                    shoot_sound.play()
                if e.key==pg.K_RETURN: 
                    fire(t2)
                    shoot_sound.play()

    keys=pg.key.get_pressed()
    if not winner:
        if keys[pg.K_a]: 
            t1.move(-speed_tank)
        if keys[pg.K_d]: 
            t1.move(speed_tank)
        if keys[pg.K_s]: 
            t1.change_angle( -speed_angle )
        if keys[pg.K_w]: 
            t1.change_angle( speed_angle )
        if keys[pg.K_q]:
            t1.jump()
        if keys[pg.K_LEFT]: 
            t2.move(-speed_tank)
        if keys[pg.K_RIGHT]: 
            t2.move(speed_tank)
        if keys[pg.K_DOWN]: 
            t2.change_angle( -speed_angle )
        if keys[pg.K_UP]: 
            t2.change_angle( speed_angle )
        if keys[pg.K_p]:
            t2.jump()
    
    for b in bullets[:]:
        b.update()
        if b.off(): 
            bullets.remove(b)
            continue
        if b.o is t1:
            opponent = t2
        else:
            opponent = t1
            
        if b.rect().colliderect(opponent.hitbox()):
            bullets.remove(b)
            opponent.has_been_hit(b.x, b.y)

            if b.o is t1: 
                score[0]+=1
            else:
                score[1]+=1
            if max(score)>=target_points: 
                if score[0]>score[1]:
                    winner = 0
                else:
                    winner = 1
                print(f"Winner: Player {winner+1}")

    # update tanks (jump physics)
    t1.update(); t2.update()
    screen.fill(BG)
    draw_terrain(screen)
    for t in [t1,t2]:
        t.draw(screen)
        if t.time_hit>0:
            t.time_hit -= 1
            ratio = t.time_hit / 60.0
            img = explosion_img.copy()
            img.set_alpha(int(255 * ratio))
            screen.blit(img, (int(t.hitX - img.get_width() / 2), int(t.hitY - img.get_height() / 2)))
        

    for b in bullets: 
        b.draw(screen)
    txt = font.render(f"{score[0]} : {score[1]}",True,(230,230,230))
    screen.blit(txt,(W//2-txt.get_width()//2,20))
    if winner is not None:
        msg = font.render(f"Tank {winner+1} gewinnt! (R = neu)",True,(255,220,120))
        screen.blit(msg,(W//2-msg.get_width()//2,H//2-20))
    if show_help:
        # Draw semi-transparent overlay with controls
        overlay = pg.Surface((W,H), pg.SRCALPHA)
        overlay.fill((0,0,0,180))
        screen.blit(overlay,(0,0))
        lines = [
            "Steuerung (Ctrl+K schliessen)",
            "Spiel verlassen: ESC",
            "Neustart (nach Sieg): R",
            "",
            "Tank 1:",
            "Bewegen: A / D",
            "Rohrwinkel: W / S",
            "Springen: Q",
            "Schiessen: SPACE",
            "",
            "Tank 2:",
            "Bewegen: Pfeil Links / Rechts",
            "Rohrwinkel: Pfeil Hoch / Runter",
            "Springen: P",
            "Schiessen: ENTER",
            f"© Cyril Wendl, {datetime.now().year}"
        ]
        pad = 8
        x = 20
        y = 20
        for line in lines:
            t = font.render(line, True, (240,240,240))
            screen.blit(t,(x,y))
            y += t.get_height() + pad
    pg.display.flip()
    clock.tick(60)

pg.quit()