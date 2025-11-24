import pygame as pg

pg.init()  # Pygame initialisieren (starten)
HEIGHT = 600  # Höhe des Fensters
WIDTH = 800  # Breite des Fensters
WINDOW = (WIDTH, HEIGHT)  # Fenstergrösse (als Tuple gespeichert)
screen = pg.display.set_mode(WINDOW)  # Fenster erstellen
pg.display.set_caption("Mein erstes Game")  # Fenstertitel setzen
clock = pg.time.Clock()  # Clock für Zeitsteuerung erstellen

running = True  # Hauptschleife
while running:
    # --- Events ---
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # --- Update --- (Spielzustand aktualisieren)

    # --- Render --- (zeichnen)
    screen.fill((30, 30, 40))
    pg.display.flip()

    # --- Zeitsteuerung ---
    clock.tick(60)  # 60 FPS

pg.quit()
