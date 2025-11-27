import math
import pygame
import matplotlib.pyplot as plt


# --- Pendulum class --------------------------------------------------------


class Pendulum:
    def __init__(self, fixation_point, length, angle, bob_radius=20, g=1500, mass=1):
        """
        fixation_point: (x, y) tuple for the fixed point on the ceiling
        length: length of the string in pixels
        angle:  initial angle from vertical in radians
        bob_radius: radius of the bob (circle)
        g: gravitational acceleration constant (pixels/(s^2))
        """
        self.fixation_point = pygame.Vector2(fixation_point)
        self.length = length
        self.angle = angle
        self.angular_velocity = 0.0
        self.angular_acceleration = 0.0

        self.bob_radius = bob_radius
        self.g = g
        self.mass = mass

        self.Ekin = []
        self.Epot = []
        self.Etot = []

    def rhs(self, x):
        # equation of motion for a simple pendulum:
        # phi''(t) = -(g / L) * sin(phi(t)) ( = rhs(phi(t)) )
        # <=> phi''(t) = f(phi(t))
        # so the rhs is equal to the angular acceleration
        return -(self.g / self.length) * math.sin(x)

    def update_euler(self, dt):
        ## Integrate (simple forward Euler) ##
        phi_old = self.angle
        self.angle += dt * self.angular_velocity
        self.angular_velocity += dt * self.rhs(phi_old)

    def update_symplectic_euler(self, dt):
        ## Integrate (symplectic Euler) ##
        self.angular_velocity += dt * self.rhs(self.angle)
        self.angle += dt * self.angular_velocity

    def update_velocity_verlet(self, dt):
        ## Integrate (velocity Verlet integration) ##
        # 1. angular acceleration at time t_{n}: phi''(t_{n}) = rhs(phi(t_{n}))
        phi_prime_prime_tn = self.rhs(self.angle)
        # 2. update phi(t_{n}) --> phi(t_{n+1})
        # phi(t_{n+1}) = phi(t_{n}) + dt * phi'(t_{n}) + 0.5 * dt**2.0 * phi''(t_{n})
        # phi(t_{n+1}) = phi(t_{n}) + dt * phi'(t_{n}) + 0.5 * dt**2.0 * f(phi(t_{n}))
        self.angle += dt * self.angular_velocity + 0.5 * dt**2.0 * phi_prime_prime_tn
        # 3. update phi'(t_{n}) --> phi'(t_{n+1})
        # phi'(t_{n+1}) = phi'(t_{n}) + 0.5 * dt * [ f(phi(t_{n})) + f(phi(t_{n+1})) ]
        self.angular_velocity += 0.5 * dt * (phi_prime_prime_tn + self.rhs(self.angle))

    def update_energies(self):
        self.Ekin.append(0.5 * self.mass * (self.length * self.angular_velocity) ** 2)
        self.Epot.append(
            self.mass * self.g * (self.length - self.length * math.cos(self.angle))
        )
        self.Etot.append(self.Ekin[-1] + self.Epot[-1])

    @property
    def bob_position(self):
        """
        Compute the (x, y) position of the bob from angle and length.
        Angle 0 means straight down.
        """
        x = self.fixation_point.x + self.length * math.sin(self.angle)
        y = self.fixation_point.y + self.length * math.cos(self.angle)
        return pygame.Vector2(x, y)

    def draw(self, surface):
        """Draw the string and the bob on the given surface."""
        bob_pos = self.bob_position

        # Draw string
        pygame.draw.line(surface, (0, 0, 0), self.fixation_point, bob_pos, 2)

        # Draw bob (filled circle)
        pygame.draw.circle(surface, (50, 50, 200), bob_pos, self.bob_radius)


# --- Basic Pygame setup & game loop ---------------------------------------


def main():
    pygame.init()

    # Window size
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pendulum Demo")

    clock = pygame.time.Clock()

    # Create a pendulum.
    # fixation_point is at the top center of the window, 100 px from the top edge.
    fixation_point = (width // 2, 100)
    length = 300  # pixels
    angle = math.radians(40)  # 30 degrees from vertical
    pendulum = Pendulum(fixation_point, length, angle)

    running = True
    while running:
        # --- Handle events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Time step in seconds
        dt = clock.tick(60) / 1000.0

        # --- update_euler game state ---
        pendulum.update_euler(dt)

        # --- update_energies ---
        pendulum.update_energies()

        # --- Draw everything ---
        screen.fill((240, 240, 240))  # light gray background

        # Optional: draw "ceiling"
        pygame.draw.line(
            screen, (0, 0, 0), (0, fixation_point[1]), (width, fixation_point[1]), 2
        )

        pendulum.draw(screen)

        pygame.display.flip()

    pygame.quit()

    # --- plot energies ---
    plt.plot(pendulum.Ekin, label="E_kin")
    plt.plot(pendulum.Epot, label="E_pot")
    plt.plot(pendulum.Etot, label="E_tot")

    plt.xlabel("Time step")
    plt.ylabel("Energy")
    plt.legend()
    plt.title("Pendulum energies over time")
    plt.show()


if __name__ == "__main__":
    main()
