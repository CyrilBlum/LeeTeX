import pygame as pg

pg.init()  # Pygame initialisieren (starten)
WINDOW = (800, 600)  # Fenstergrösse (als Tuple gespeichert)
screen = pg.display.set_mode(WINDOW)  # Fenster erstellen
icon = pg.image.load("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/icon.png")
pg.display.set_caption("Mein erstes Game")  # Fenstertitel setzen
pg.display.set_icon(icon)

background_color = (50, 80, 120)

clock = pg.time.Clock()  # Clock für Zeitsteuerung erstellen

# Spieler-Rect und Geschwindigkeit
player = pg.Rect(100, 100, 50, 50)
speed = 5

running = True  # Hauptschleife
while running:
    # --- Events ---
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # --- Update (Input/Bewegung) ---
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        player.x -= speed
    if keys[pg.K_RIGHT]:
        player.x += speed
    if keys[pg.K_UP]:
        player.y -= speed
    if keys[pg.K_DOWN]:
        player.y += speed
    player.clamp_ip(screen.get_rect())  # im Fenster halten

    # --- Render --- (zeichnen)
    screen.fill(background_color)  # Hintergrundfarbe setzen
    pg.draw.rect(screen, (255, 255, 255), player)  # Spieler zeichnen

    pg.display.flip()

    # --- Zeitsteuerung ---
    clock.tick(60)  # 60 FPS

pg.quit()
