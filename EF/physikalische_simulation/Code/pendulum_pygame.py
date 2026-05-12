import math
import pygame
import matplotlib.pyplot as plt


# --- Pendulum class --------------------------------------------------------
class Pendulum:
    def __init__(self, fixation_point, length, angle, g=1500, mass=1):
        self.fixation_point = pygame.Vector2(fixation_point)
        self.length = length
        self.angle = angle
        self.angular_velocity = 0.0
        self.g = g
        self.mass = mass

        # Speicher für die Energie-Historie
        self.Ekin = []
        self.Epot = []
        self.Etot = []

    def rhs(self, phi):
        """Differentialgleichung: phi''(t) = -g/L * sin(phi(t))"""

        return -(self.g / self.length) * math.sin(phi)

    # --- 1. Expliziter Euler (instabil, Energie steigt) ---
    def update_euler(self, dt):
        phi_old = self.angle
        v_old = self.angular_velocity

        self.angle += dt * v_old
        self.angular_velocity += dt * self.rhs(phi_old)

    # --- 2. Symplektischer Euler (stabil, Energie oszilliert leicht) ---
    def update_symplectic_euler(self, dt):
        # Erst Geschwindigkeit, dann Position mit NEUER Geschwindigkeit
        self.angular_velocity += dt * self.rhs(self.angle)
        self.angle += dt * self.angular_velocity

    # --- 3. Velocity-Verlet (sehr stabil & genau) ---
    def update_velocity_verlet(self, dt):
        a_n = self.rhs(self.angle)

        # Positionsschritt
        self.angle += dt * self.angular_velocity + 0.5 * dt**2 * a_n

        # Neuer Beschleunigungsschritt
        a_next = self.rhs(self.angle)

        # Geschwindigkeitsschritt
        self.angular_velocity += 0.5 * dt * (a_n + a_next)

    def update_energies(self):
        v_linear = self.length * self.angular_velocity
        e_kin = 0.5 * self.mass * v_linear**2
        e_pot = self.mass * self.g * (self.length - self.length * math.cos(self.angle))
        self.Ekin.append(e_kin)
        self.Epot.append(e_pot)
        self.Etot.append(e_kin + e_pot)

    def draw(self, surface):
        bob_pos = (
            self.fixation_point.x + self.length * math.sin(self.angle),
            self.fixation_point.y + self.length * math.cos(self.angle),
        )
        pygame.draw.line(surface, (100, 100, 100), self.fixation_point, bob_pos, 2)
        pygame.draw.circle(
            surface, (50, 50, 200), (int(bob_pos[0]), int(bob_pos[1])), 20
        )


# --- Simulation Setup ------------------------------------------------------
def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Vergleich: Euler vs. Verlet")
    clock = pygame.time.Clock()

    # Initialisierung
    pendulum = Pendulum((width // 2, 100), 300, math.radians(60))

    # DIDAKTISCH WICHTIG: Fester Zeitschritt für physikalische Korrektheit
    dt = 1.0 / 60.0

    # Wähle hier das Verfahren zum Testen aus:
    # 1: update_euler
    # 2: update_symplectic_euler
    # 3: update_velocity_verlet
    METHOD = 3

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Physik-Integration
        if METHOD == 1:
            pendulum.update_euler(dt)
        elif METHOD == 2:
            pendulum.update_symplectic_euler(dt)
        else:
            pendulum.update_velocity_verlet(dt)

        pendulum.update_energies()

        # Grafik
        screen.fill((240, 240, 240))
        pendulum.draw(screen)

        # Info-Text auf Screen
        font = pygame.font.SysFont(None, 24)
        img = font.render(
            f"Methode: {['Euler', 'Symp. Euler', 'Verlet'][METHOD-1]}", True, (0, 0, 0)
        )
        screen.blit(img, (20, 20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

    # --- Analyse-Plot ---
    plt.figure(figsize=(10, 6))
    plt.plot(pendulum.Etot, label="Gesamtenergie (Etot)", color="black", linewidth=1.5)
    plt.plot(pendulum.Ekin, label="Kinetisch (Ekin)", alpha=0.4)
    plt.plot(pendulum.Epot, label="Potentiell (Epot)", alpha=0.4)

    # Zeige die Drift/Abweichung deutlich
    plt.axhline(y=pendulum.Etot[0], color="r", linestyle="--", label="Startenergie")

    plt.title(
        f"Energieverlauf: {['Expliziter Euler', 'Symplektischer Euler', 'Velocity-Verlet'][METHOD-1]}"
    )
    plt.xlabel("Zeitschritte")
    plt.ylabel("Energie")
    plt.legend(loc="upper right")
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == "__main__":
    main()
