import pygame as pg
import random as r
import math as m
from flipper import *



# --- Sounds ---
bg_sound = pg.mixer.Sound("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/retro-arcade-game-music.mp3")
bounce_sound = pg.mixer.Sound("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/pinball35.mp3")
tube_sound = pg.mixer.Sound("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/pinball8.mp3")
#bg_sound.play(loops=-1)
collect_points = pg.mixer.Sound("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/collectpoints.mp3")


# --- Flipper-Spezialelemente ---
tube = pg.image.load("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/tube.png").convert_alpha()
tube = pg.transform.smoothscale(tube, (100, tube.get_height() * 100 // tube.get_width()))
tube_rect = pg.Rect(20, tube.get_height()+20, 30, 40) # Bereich unter dem Rohr
tube_hit = False
tube_timer = 0

# --- Spielfiguren / Objekte ---
ball = pg.Rect(WIDTH // 2 - 8, 300, 16, 16)
wall_l = pg.Rect(0, 0, 20, HEIGHT)
wall_r = pg.Rect(WIDTH - 20, 0, 20, HEIGHT)
floor = pg.Rect(0, HEIGHT - 20, WIDTH, 20)
objects = []

# --- Spezielle Objekte ---
obj_stick = StickObj(
    position = (WIDTH*.2, 133),
    width = 30,
    height = 30,
    color = (255, 0, 255)
)

# --- Ball Bewegungsvariablen ---
step_bally = 0
step_ballx = r.choice((-1, 1)) * r.uniform(3, 5)

# --- Flipper ---
flipper_left = Flipper(
    start_base = (20, HEIGHT-130),
    length = WIDTH*.45,
    start_angle = -20,
    max_up_angle = 40,
    speed = int(8/SPEEDUP*(WIDTH/800)),
    width = 20,
    color = (100, 100, 100),
    bounceback_factor=5,
    flipper_type="left"
)

flipper_right = Flipper(
    start_base = (WIDTH - 20, HEIGHT-130),
    length = WIDTH*.45,
    start_angle = -160,
    max_up_angle = -40,
    speed = int(8/SPEEDUP*(WIDTH/800)),
    width = 20,
    color = (100, 100, 100),
    bounceback_factor=5,
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
                step_ballx = r.choice((-1, 1)) * r.uniform(3, 5)
                objects = []

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
                    step_ballx -= (flipper.current_angle * 0.1/SPEEDUP)*2
                else:
                    step_ballx += -(flipper.current_angle + 180) * 0.1/SPEEDUP*2
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
            objects.append(CollectObj(
                position = (r.randint(40, WIDTH-40), r.randint(40, HEIGHT-200)),
                radius = 30,
                color = (255, 215, 0)
                )
            )

        for o in objects[:]:
            if not o.collected and ball.colliderect(o.rect):
                o.collected = True
                score += 1
                collect_points.play()
            if o.collected:
                objects.remove(o)

        if ball.colliderect(obj_stick.rect):
            obj_stick.was_hit()

        # --- Physik-Update ---
        step_bally += GRAVITY

        # sticky place
        ball, score, step_ballx, step_bally = obj_stick.update(ball, score, step_ballx, step_bally)

        # check if ball hits lower end of tube
        pixel_x = ball.centerx - 20 # tube starts at x=20
        pixel_y = ball.centery - 20 # tube starts at y=20

        pixel_next_x = pixel_x + int(step_ballx)
        pixel_next_y = pixel_y + int(step_bally)
        if ball.colliderect(tube_rect):
            print("Tube hit")
            score += 10
            tube_sound.play(fade_ms=50)
            tube_hit = True
            ball.bottom = tube_rect.top  # place ball on top of tube exit
            ball.centerx = tube_rect.centerx
            step_bally = -10
            pixel_next_y = pixel_y + int(step_bally)
            
            if pixel_next_x < 0 or pixel_next_x >= tube.get_width() or pixel_next_y < 0 or pixel_next_y >= tube.get_height():
                # Out of tube bounds, reverse direction
                step_ballx = -step_ballx
                step_bally = -step_bally
                print("Out of tube bounds - reverse")
                continue

        # if ball is within tube, check pixel transparency and move ball along tube
        if tube_hit:
            tube_timer += 1
            if 0 <= pixel_next_x < tube.get_width() and 0 <= pixel_next_y < tube.get_height():
                alpha = tube.get_at((pixel_next_x, pixel_next_y))[3]

                if alpha > 128:  # Inside non-transparent area
                    # Continue in current direction
                    print("Will stay inside tube - continue")
                    step_bally -= GRAVITY
                else:
                    print("Tube bounce")
                    # Find non-transparent direction
                    directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
                    for dx, dy in directions:
                        test_x = pixel_x + dx * 5
                        test_y = pixel_y + dy * 5
                        if 0 <= test_x < tube.get_width() and 0 <= test_y < tube.get_height():
                            print(f"Testing direction {dx}, {dy}")
                            if tube.get_at((test_x, test_y))[3] > 128:
                                print(f"Found exit direction {dx}, {dy}")
                                step_ballx = dx * 2
                                step_bally = dy * 2
                                break
            else:
                # Out of tube bounds, reverse direction
                tube_hit = False
                tube_timer = 0
            
        print(tube_timer)

            #step_ballx = r.choice((-1, 1)) * r.uniform(3, 5)

        # --- Ball-Update ---
        ball.x += step_ballx
        ball.y += step_bally

    # --- Zeichnen ---
    screen.fill((255, 255, 255))
    if not gameover:
        # Spezialelemente
        mask = pg.mask.from_surface(tube)
        #c_mask = mask.to_surface(setcolor=(0,0,0), unsetcolor=(0,0,0,0))
        #tube_colored.blit(c_mask, (0,0))
        screen.blit(tube, (20, 20))

        pg.draw.rect(screen, (100, 100, 255), tube_rect)  # Bereich unter dem Rohr

        flipper_left.update()
        flipper_right.update()

        # Ball
        pg.draw.circle(screen, (255, 0, 0), (ball.centerx, ball.centery), ball.width / 2)

        # beweglicher Flipper
        flipper_left.draw(screen)
        flipper_right.draw(screen)

        # Objekte 
        for o in objects:
            if not o.collected:
                o.draw(screen)
                

        obj_stick.draw(screen)
    

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
