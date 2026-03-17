import pygame as pg
import random

pg.init()  # Pygame initialisieren (starten)
WINDOW = (800, 600)  # Fenstergrösse (als Tuple gespeichert)
screen = pg.display.set_mode(WINDOW)  # Fenster erstellen
pg.display.set_caption("Mein erstes Game")  # Fenstertitel setzen
icon = pg.image.load("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/icon.png")
pg.display.set_icon(icon)
clock = pg.time.Clock()  # Clock für Zeitsteuerung erstellen

running = True  # Hauptschleife
while running:
    # --- Events ---
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # --- render (zeichnen) --- 
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    background_color = (r, g, b)
    screen.fill(background_color)  # Hintergrundfarbe setzen

    pg.display.flip()

    # --- Zeitsteuerung ---
    clock.tick(10)  # 10 FPS

pg.quit()
