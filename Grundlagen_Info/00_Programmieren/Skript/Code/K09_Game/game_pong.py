import pygame as pg
import random
pg.init()

info = pg.display.Info() # Informationen zum aktuellen Geräte-Display abrufen
print(info)

WIDTH = info.current_w # verwende doppelte Auflösung für bessere Qualität auf hochauflösenden Displays
HEIGHT = info.current_h # verwende doppelte Auflösung für bessere Qualität auf hochauflösenden Displays
FPS = 120 # Ziel-Bildwiederholrate

screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
pg.display.set_caption("Pong")

background_color = (50, 80, 120)

# Schläger
paddle_w = WIDTH * 0.02
paddle_h = HEIGHT // 5
paddle_speed = WIDTH * 0.01 / (FPS/60)
left_paddle = pg.Rect(30, HEIGHT // 2 - paddle_h // 2, paddle_w, paddle_h)
right_paddle = pg.Rect(WIDTH - 30 - paddle_w, HEIGHT // 2 - paddle_h // 2, paddle_w, paddle_h)

# Ball (als Rechteck)
ball_size = WIDTH * 0.02
ball = pg.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size) # ball startet in der Mitte
ball_speed = WIDTH * 0.008 / (FPS/60)
# Geschwindigkeit als separate Variablen
ball_speed_x = random.choice((-1, 1)) * ball_speed
ball_speed_y = random.choice((-1, 1)) * ball_speed

# Spielstand
left_score = 0
right_score = 0
font = pg.font.Font(None, int(HEIGHT * 0.1))

# Sounds
bg_sound = pg.mixer.Sound("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/retro-arcade-game-music.mp3")
bounce_sound = pg.mixer.Sound("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/laser.mp3")
score_sound = pg.mixer.Sound("Grundlagen_Info/12_Pygame_CE/Project_Files/Platform/audio/shoot.wav")

# Hintergrundmusik
bg_sound.play(loops=-1)

# Clock
clock = pg.time.Clock()


def reset_ball(direction: int):
    """Ball zentrieren und in die angegebene Richtung starten (-1 links, +1 rechts)."""
    ball.center = (WIDTH // 2, HEIGHT // 2)
    global ball_speed_x, ball_speed_y
    ball_speed_x = direction * ball_speed
    ball_speed_y = random.choice((-1, 1)) * ball_speed


def reset_match():
    """Spielstand, Schläger und Ball zurücksetzen, um ein neues Spiel zu starten."""
    global left_score, right_score
    left_score = 0
    right_score = 0
    left_paddle.centery = HEIGHT // 2
    right_paddle.centery = HEIGHT // 2
    reset_ball(direction=random.choice((-1, 1)))


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            # R zum kompletten Zurücksetzen; ESC zum Beenden
            if event.key == pg.K_r:
                reset_match()
            elif event.key == pg.K_ESCAPE:
                running = False


    # Steuerung der Schläger
    keys = pg.key.get_pressed()
    # Linker Schläger: W/S
    if keys[pg.K_w]:
        left_paddle.y -= paddle_speed
    if keys[pg.K_s]:
        left_paddle.y += paddle_speed
    # Rechter Schläger: Pfeil hoch/runter
    if keys[pg.K_UP]:
        right_paddle.y -= paddle_speed
    if keys[pg.K_DOWN]:
        right_paddle.y += paddle_speed

    # Schläger auf Bildschirm begrenzen
    left_paddle.clamp_ip(screen.get_rect())
    right_paddle.clamp_ip(screen.get_rect())

    # Ball bewegen
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Abprallen an Ober-/Unterkante
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
        bounce_sound.play()

    # Kollisionen mit Schlägern
    if ball.colliderect(left_paddle):
        ball_speed_x *= -1
        # Variation je nach Trefferposition hinzufügen
        offset = (ball.centery - left_paddle.centery) / (paddle_h / 2)
        # Auf [-ball_speed, ball_speed] begrenzen und als Skalar beibehalten
        ball_speed_y = max(-ball_speed, min(ball_speed, ball_speed * offset))
        bounce_sound.play()

    if ball.colliderect(right_paddle):
        ball_speed_x *= -1
        offset = (ball.centery - right_paddle.centery) / (paddle_h / 2)
        ball_speed_y = max(-ball_speed, min(ball_speed, ball_speed * offset))
        bounce_sound.play()

    # Punktewertung
    if ball.right < 0:
        right_score += 1
        score_sound.play()
        reset_ball(direction=1)
    elif ball.left > WIDTH:
        left_score += 1
        score_sound.play()
        reset_ball(direction=-1)

    # Zeichnen
    screen.fill(background_color)
    # Mittellinie
    pg.draw.line(screen, (255, 255, 255), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), int(WIDTH*0.005))
    # Schläger und Ball
    pg.draw.rect(screen, (240, 220, 90), left_paddle)
    pg.draw.rect(screen, (240, 220, 90), right_paddle)
    pg.draw.rect(screen, (200, 60, 60), ball)

    # Spielstandsanzeige
    score_text = f"{left_score} : {right_score}"
    score_surf = font.render(score_text, True, (255, 255, 255))
    score_rect = score_surf.get_rect(center=(WIDTH // 2, HEIGHT * 0.1))
    screen.blit(score_surf, score_rect)

    pg.display.flip()
    clock.tick(FPS)

pg.quit()