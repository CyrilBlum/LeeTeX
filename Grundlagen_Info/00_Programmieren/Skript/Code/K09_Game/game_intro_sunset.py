import pygame as pg

pg.init()  # Pygame initialisieren (starten)
HEIGHT = 600  # Höhe des Fensters
WIDTH = 800  # Breite des Fensters
WINDOW = (WIDTH, HEIGHT)  # Fenstergrösse (als Tuple gespeichert)
screen = pg.display.set_mode(WINDOW)  # Fenster erstellen
icon = pg.image.load("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/icon.png")
pg.display.set_caption("Mein erstes Game")  # Fenstertitel setzen
pg.display.set_icon(icon)

background_color = (50, 80, 120)
sun_y = HEIGHT // 3

clock = pg.time.Clock()  # Clock für Zeitsteuerung erstellen

running = True  # Hauptschleife
while running:
    # --- Events ---
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # --- Render --- (zeichnen)
    screen.fill(background_color)  # Hintergrundfarbe setzen
    # Himmel (einfacher Gradient)
    for y in range(0, HEIGHT // 2):
        c = 100 + int(155 * (y / (HEIGHT // 2)))  # 100..255
        pg.draw.rect(screen, (c, 120, 180), (0, y, WIDTH, 1))

    # Sonne sinkt langsam (maximal bis zum Meer)
    if sun_y < (HEIGHT // 2 + 60):
        sun_y += 0.5  # y-Position der Sonne verändern

    # Sonne
    pg.draw.circle(screen, (255, 200, 0), (WIDTH // 2, sun_y), 60)

    # Meer
    pg.draw.rect(screen, (20, 80, 160), (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    # Bildschirm aktualisieren
    pg.display.flip()

    # --- Zeitsteuerung ---
    clock.tick(60)  # 60 FPS

pg.quit()
