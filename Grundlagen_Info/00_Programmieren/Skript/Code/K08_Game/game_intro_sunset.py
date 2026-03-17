import pygame as pg

pg.init()  # Pygame initialisieren (starten)
HEIGHT = 600  # Höhe des Fensters
WIDTH = 800  # Breite des Fensters
WINDOW = (WIDTH, HEIGHT)  # Fenstergrösse (als Tuple gespeichert)
screen = pg.display.set_mode(WINDOW)  # Fenster erstellen
pg.display.set_caption("Sonnenuntergang")  # Fenstertitel setzen
icon = pg.image.load("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/icon.png")
pg.display.set_icon(icon)
clock = pg.time.Clock()  # Clock für Zeitsteuerung erstellen

sun_center_x = WIDTH // 2 # x-Koorinate Kreismittelpunkt Sonne
sun_center_y = HEIGHT // 3 # y-Koorinate Kreismittelpunkt Sonne
sun_radius = 60 # Radius der Sonne

running = True  # Hauptschleife
while running:
    # --- Events ---
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # --- Update & Render ---
    # Himmel (einfacher Gradient)
    for y in range(0, HEIGHT // 2):
        red = 100 + int(155 * (y / (HEIGHT // 2)))  # 100 ... 255
        pg.draw.rect(screen, (red, 120, 180), (0, y, WIDTH, 1))

    # Sonne sinkt langsam (maximal bis zum Meer)
    # nicht mehr sichtbare Sonne soll nicht mehr berechnet werden
    if sun_center_y < (HEIGHT // 2 + sun_radius):
        sun_center_y += 0.5  # y-Position der Sonne verändern
        # Sonne
        pg.draw.circle(screen, (255, 200, 0), (sun_center_x, sun_center_y), sun_radius)

    # Meer
    pg.draw.rect(screen, (20, 80, 160), (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    # Bildschirm aktualisieren
    pg.display.flip()

    # --- Zeitsteuerung ---
    clock.tick(60)  # 60 FPS

pg.quit()
