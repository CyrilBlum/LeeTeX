import pygame as pg

pg.init()  # Pygame initialisieren (starten)
WINDOW = (800, 600)  # Fenstergrösse (als Tuple gespeichert)
screen = pg.display.set_mode(WINDOW)  # Fenster erstellen
icon = pg.image.load("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/icon.png")
pg.display.set_caption("Mein erstes Game")  # Fenstertitel setzen
pg.display.set_icon(icon)
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
