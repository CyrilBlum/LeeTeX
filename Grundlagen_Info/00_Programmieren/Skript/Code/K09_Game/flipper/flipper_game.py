import pygame as pg
import random as r
import math as m
from flipper import *

# --- Initialisierung ---
pg.init()
pg.mixer.init()

HEIGHT = 800
WIDTH = 500
WINDOW = (WIDTH, HEIGHT)
FPS = 60
SPEEDUP = FPS/60

screen = pg.display.set_mode(WINDOW)
pg.display.set_caption("flipper")
clock = pg.time.Clock()
font = pg.font.Font(None, 36)

# --- Sounds ---
pg.mixer.init()
bg_sound = pg.mixer.Sound("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/retro-arcade-game-music.mp3")
bounce_sound = pg.mixer.Sound("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/laser.mp3")
bg_sound.play(loops=-1)
collect_points = pg.mixer.Sound("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/collectpoints.mp3")

# --- Spielfiguren / Objekte ---
ball = pg.Rect(WIDTH // 2 - 8, 300, 16, 16)
wall_l = pg.Rect(0, 0, 20, HEIGHT)
wall_r = pg.Rect(WIDTH - 20, 0, 20, HEIGHT)
floor = pg.Rect(0, HEIGHT - 20, WIDTH, 20)
objects = []

# --- Ball Bewegungsvariablen ---
step_bally = 0
step_ballx = r.choice((-1, 1)) * r.uniform(2, 5)

# --- Flipper ---
flipper_left = Flipper(
    start_base = (20, HEIGHT-100),
    length = 200,
    start_angle = -20,
    max_up_angle = 40,
    speed = 5/SPEEDUP,
    width = 20,
    color = (0, 255, 0),
    bounceback_factor=3,
    flipper_type="left"
)

flipper_right = Flipper(
    start_base = (WIDTH - 20, HEIGHT-100),
    length = 200,
    start_angle = -160,
    max_up_angle = -40,
    speed = 5/SPEEDUP,
    width = 20,
    color = (0, 0, 255),
    bounceback_factor=3,
    flipper_type="right"
)

# Highscore-Schrift
font = pg.font.Font(None, 36)
score = 0

# --- Physik ----
FRICTION = 0.75/SPEEDUP
GRAVITY = 1/SPEEDUP

# Spielzustand
gameover = False

running = True
timer = 0
# --- Hauptschleife ---
while running:
    # --- Events ---
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                if gameover:
                    gameover = False
                    score = 0
                # reset ball
                ball.x = WIDTH // 2 - 8
                ball.y = 300
                step_bally = 0
                step_ballx = r.choice((-1, 1)) * r.random() * 5

    # --- Tastaturstatus ---
    if not gameover: 
        keys = pg.key.get_pressed()

        # --- Flipper steuern (Taste O) ---
        if keys[pg.K_LEFT]:
            flipper_left.update_angle(True)
        elif keys[pg.K_RIGHT]:
            flipper_right.update_angle(True)
        else:
            flipper_left.update_angle(False)
            flipper_right.update_angle(False)

        # --- Mögliche Spiel-Ereignisse überprüfen ---
        # --- Kollision mit Flipper ---
        for flipper in [flipper_left, flipper_right][:]:
            if flipper.collides_with_ball(ball) and step_bally > 0:  # nur wenn Ball von oben fällt
                # Wir nehmen die Unterseite der Kugel (nicht die linke obere Ecke)
                y_flipper = flipper.get_y_at_x(ball.centerx, top=True)

                # Ball genau auf den Flipper setzen
                ball.bottom = y_flipper

                # Bounce nach oben, Dämpfung
                step_bally = -step_bally*FRICTION
                step_bally -= flipper.get_speed_at_x(ball.centerx)*flipper.bounceback_factor

                # Änderung der x-Richtung basierend auf Flipper-Winkel
                if flipper.flipper_type == "left":
                    step_ballx -= (flipper.current_angle * 0.1/SPEEDUP)
                    print(f"Adding {-(flipper.current_angle * 0.1/SPEEDUP)} to step_ballx")
                else:
                    step_ballx += -(flipper.current_angle + 180) * 0.1/SPEEDUP
                    print(f"Adding {-(flipper.current_angle + 180) * 0.1/SPEEDUP} to step_ballx")
        # --- Kollision mit Boden ---
        if ball.bottom >= floor.top:
            gameover = True

        # --- Kollision mit Wänden (links) ---
        if ball.left <= wall_l.right:
            ball.left = wall_l.right
            bounce_sound.play(fade_ms=50)
            step_ballx = abs(step_ballx) * FRICTION

        # --- Kollision mit Wänden (rechts) ---
        if ball.right >= wall_r.left:
            ball.right = wall_r.left
            bounce_sound.play(fade_ms=50)
            step_ballx = -abs(step_ballx) * FRICTION

        timer += 1
        if timer % 60 == 0:
            print("Adding new object")
            objects.append(CollectObj(
                position = (r.randint(40, WIDTH-40), r.randint(40, HEIGHT-200)),
                radius = 10,
                color = (255, 215, 0)
                )
            )

        for o in objects[:]:
            if not o.collected and ball.collidepoint(o.position):
                o.collected = True
                score += 1
                collect_points.play()
            if o.collected:
                objects.remove(o)

        
        # --- Ball-Update ---
        ball.x += step_ballx
        step_bally += GRAVITY
        ball.y += step_bally

    # --- Zeichnen ---
    screen.fill((255, 255, 255))
    if not gameover:
        flipper_left.update()
        flipper_right.update()

        # Ball
        pg.draw.circle(screen, (255, 0, 0), (ball.centerx, ball.centery), ball.width / 2)

        # beweglicher Flipper
        flipper_left.draw(screen)
        flipper_right.draw(screen)

        # Objekte 
        for o in objects:
            o.draw(screen)

        # Score anzeigen
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # Wände und Boden
        pg.draw.rect(screen, (0, 0, 0), floor)
        pg.draw.rect(screen, (0, 0, 0), wall_l)
        pg.draw.rect(screen, (0, 0, 0), wall_r)
    
    else:
        # Game Over Bildschirm
        game_over_text = font.render("GAME OVER\n Press R to restart", True, (255, 0, 0))
        score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))

    pg.display.flip()
    clock.tick(FPS)

pg.quit()
