import pygame

# Initialisierung
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# --- Setup der Spielfigur ---
# Wir nutzen Vector2 für die Position, um Kommazahlen (Floats) zu speichern.
# Ein normales pygame.Rect speichert nur ganze Zahlen (Integers),
# was bei kleinen dt-Werten die Bewegung "schlucken" würde.
player_pos = pygame.Vector2(400, 300)
player_speed = 300  # Geschwindigkeit: 300 Pixel pro Sekunde

player_rect = pygame.Rect(0, 0, 50, 50)

while running:
    # 1. Delta Time berechnen
    # clock.tick(60) begrenzt auf 60 FPS und gibt die Zeit in Millisekunden zurück.
    # Wir teilen durch 1000, um Sekunden zu erhalten (z.B. 0.016 s).
    dt = clock.tick(60) / 1000.0

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# 
    # 2. Bewegung mit Delta Time
    keys = pygame.key.get_pressed()

    # Wenn dt z.B. 0.016 ist, rechnen wir: 300 Pixel / Sekunde * 0.016 Sekunden = 4.8 Pixel Bewegung
    
    if keys[pygame.K_LEFT]:
        player_pos.x -= player_speed * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += player_speed * dt
    if keys[pygame.K_UP]:
        player_pos.y -= player_speed * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += player_speed * dt

    # 3. Position auf das Rect übertragen (fürs Zeichnen / Kollision)
    player_rect.center = player_pos

    # Zeichnen
    screen.fill("black")
    pygame.draw.rect(screen, "red", player_rect)
    pygame.display.flip()

    # Optional: FPS im Titel anzeigen, um zu sehen, dass die Geschwindigkeit gleich bleibt
    pygame.display.set_caption(f"FPS: {clock.get_fps():.2f}")

pygame.quit()
