import pygame as pg

pg.init() # Pygame initialisieren (starten)
WINDOW = (800, 600) # Fenstergrösse (als Tuple gespeichert)
screen = pg.display.set_mode(WINDOW) # Fenster erstellen
icon = pg.image.load("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/icon.png")
pg.display.set_caption("Mein erstes Game") # Fenstertitel setzen
pg.display.set_icon(icon)

background_color = (50, 80, 120)

clock = pg.time.Clock() # Clock für Zeitsteuerung erstellen

# Liste für Kreise
mouse_positions = []  # Liste für Maus-Klick-Positionen

running = True # Hauptschleife
while running:
	# --- Events ---
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		elif event.type == pg.KEYDOWN or event.type == pg.K_ESCAPE:
			running = False
		elif event.type == pg.MOUSEBUTTONDOWN:
			x, y = event.pos
			mouse_positions.append((x, y))

	# --- Render --- (zeichnen)
	screen.fill(background_color) # Hintergrundfarbe setzen

	# Kreise zeichnen
	# In der Game-Loop, im Render-Abschnitt:
	for pos in mouse_positions:
		pg.draw.circle(screen, (255, 100, 100), pos, 10)

	pg.display.flip()

	# --- Zeitsteuerung ---
	clock.tick(60)  # 60 FPS

pg.quit()