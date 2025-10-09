import pygame as pg

pg.init() # Pygame initialisieren (starten)
WIDTH, HEIGHT = 800, 600 # Fenstergrösse
screen = pg.display.set_mode((WIDTH, HEIGHT)) # Fenster erstellen
icon = pg.image.load("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/icon.png")
pg.display.set_caption("Mein erstes Game") # Fenstertitel setzen
pg.display.set_icon(icon)

background_color = (50, 80, 120)

clock = pg.time.Clock() # Clock für Zeitsteuerung erstellen

# Liste für Kreise
circles = []

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
			circles.append((x, y))

	# --- Render --- (zeichnen)
	screen.fill(background_color) # Hintergrundfarbe setzen

	# Kreise zeichnen
	for x, y in circles:
		pg.draw.circle(screen, (255, 100, 100), (x, y), 10)

	pg.display.flip()

	# --- Zeitsteuerung ---
	clock.tick(60)  # 60 FPS

pg.quit()