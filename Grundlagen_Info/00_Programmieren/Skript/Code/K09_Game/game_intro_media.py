import pygame as pg
from pathlib import Path

pg.init()  # Pygame initialisieren (starten)
WIDTH = 800
HEIGHT = 600
WINDOW = (WIDTH, HEIGHT)  # Fenstergrösse (als Tuple gespeichert)
screen = pg.display.set_mode(WINDOW)  # Fenster erstellen

base_dir = Path(__file__).parent
icon = pg.image.load(base_dir / "icon.png")
pg.display.set_caption("Mein erstes Game")  # Fenstertitel setzen
pg.display.set_icon(icon)

# Medien laden (Bild und Sound)
assets = base_dir / "assets"
img = pg.image.load(assets / "player.jpeg")
# Skalieren auf bestimmte Höhe, Seitenverhältnis beibehalten
desired_height = 100
aspect_ratio = img.get_width() / img.get_height()
new_width = int(desired_height * aspect_ratio)
img = pg.transform.scale(img, (new_width, desired_height))

# Spieler-Rect für Position/Kollision
player = img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Einfaches Item als farbiges Quadrat
item_surf = pg.Surface((40, 40), pg.SRCALPHA)
item_surf.fill((255, 200, 0))
item = item_surf.get_rect(center=(WIDTH // 3, HEIGHT // 2))

# Sound laden
try:
    pg.mixer.init()
    motor = pg.mixer.Sound(assets / "motor.mp3")
except Exception:
    motor = None  # falls kein Audio verfügbar ist

background_color = (50, 80, 120)
clock = pg.time.Clock()  # Clock für Zeitsteuerung erstellen

running = True  #  Hauptschleife
collided = False
speed = 5

while running:
    # --- Events ---
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # --- Update ---
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        player.x -= speed
    if keys[pg.K_RIGHT]:
        player.x += speed
    if keys[pg.K_UP]:
        player.y -= speed
    if keys[pg.K_DOWN]:
        player.y += speed

    # Im Fenster halten
    player.clamp_ip(screen.get_rect())

    # Kollision + Sound
    if player.colliderect(item):
        if not collided and motor:
            motor.play()
        collided = True
    else:
        collided = False

    # --- Render --- (zeichnen)
    screen.fill(background_color)  # Hintergrundfarbe setzen

    # Item und Spieler zeichnen
    screen.blit(item_surf, item)
    # optional: Rotation -> pg.transform.rotate(img, angle)
    screen.blit(img, player)

    pg.display.flip()

    # --- Zeitsteuerung ---
    clock.tick(60)  # 60 FPS

pg.quit()
