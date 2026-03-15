import pygame
import random
import time

# --- KONFIGURATION ---
WIDTH, HEIGHT = 1024, 768  # Etwas größeres Fenster für den Beamer
PARTICLE_COUNT = 1500      # 1500 ist meist der "Sweet Spot" für den Lag-Effekt
PARTICLE_RADIUS = 3
COLLISION_DISTANCE = 6
USE_EFFICIENT_ALGO = False 

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Laufzeit-Vergleich: Kollisionserkennung")

# Schrift-Setup: Größer und Grün
FONT_SIZE = 36
TEXT_COLOR = (0, 255, 0) # Leuchtendes Grün
font = pygame.font.SysFont("Arial", FONT_SIZE, bold=True)

class Particle:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.vx = random.uniform(-1.5, 1.5)
        self.vy = random.uniform(-1.5, 1.5)
        self.color = (255, 255, 255)

    def move(self):
        self.x = (self.x + self.vx) % WIDTH
        self.y = (self.y + self.vy) % HEIGHT
        self.color = (255, 255, 255)

particles = [Particle() for _ in range(PARTICLE_COUNT)]

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((10, 10, 10)) # Dunkler Hintergrund für besseren Kontrast
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            USE_EFFICIENT_ALGO = not USE_EFFICIENT_ALGO

    # 1. Bewegung
    for p in particles:
        p.move()

    checks = 0
    start_time = time.perf_counter()

    # 2. Kollisionserkennung
    if not USE_EFFICIENT_ALGO:
        # INEFFIZIENT: O(n^2)
        for i in range(len(particles)):
            for j in range(i + 1, len(particles)):
                checks += 1
                dx = particles[i].x - particles[j].x
                dy = particles[i].y - particles[j].y
                if dx*dx + dy*dy < COLLISION_DISTANCE**2:
                    particles[i].color = (255, 0, 0)
                    particles[j].color = (255, 0, 0)
    else:
        # EFFIZIENT: O(n) mit Grid
        grid_size = COLLISION_DISTANCE * 1.5
        grid = {}
        for p in particles:
            cell = (int(p.x / grid_size), int(p.y / grid_size))
            if cell not in grid: grid[cell] = []
            grid[cell].append(p)
        
        for cell_coords, cell_particles in grid.items():
            cx, cy = cell_coords
            for i in range(len(cell_particles)):
                for dx_grid in [-1, 0, 1]:
                    for dy_grid in [-1, 0, 1]:
                        neighbor_cell = (cx + dx_grid, cy + dy_grid)
                        if neighbor_cell in grid:
                            for p_other in grid[neighbor_cell]:
                                if cell_particles[i] is p_other: continue
                                checks += 1
                                dx = cell_particles[i].x - p_other.x
                                dy = cell_particles[i].y - p_other.y
                                if dx*dx + dy*dy < COLLISION_DISTANCE**2:
                                    cell_particles[i].color = (255, 0, 0)

    calc_time = (time.perf_counter() - start_time) * 1000

    # 3. Zeichnen
    for p in particles:
        pygame.draw.circle(screen, p.color, (int(p.x), int(p.y)), PARTICLE_RADIUS)

    # Info-Anzeige (Grün & Groß)
    mode_str = "EFFIZIENT (Grid)" if USE_EFFICIENT_ALGO else "INEFFIZIENT (Brute Force)"
    
    # Texte rendern
    text_mode = font.render(f"MODUS: {mode_str}", True, TEXT_COLOR)
    text_info = font.render(f"Teilchen: {PARTICLE_COUNT} | Vergleiche: {checks:,}", True, TEXT_COLOR)
    text_perf = font.render(f"Zeit: {calc_time:.1f}ms | FPS: {int(clock.get_fps())}", True, TEXT_COLOR)
    text_hint = font.render("LEERTASTE zum Wechseln", True, (200, 200, 200)) # Etwas dezenter

    # Auf den Screen blitten (Abstände vergrößert)
    screen.blit(text_mode, (20, 20))
    screen.blit(text_info, (20, 70))
    screen.blit(text_perf, (20, 120))
    screen.blit(text_hint, (20, HEIGHT - 60))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()