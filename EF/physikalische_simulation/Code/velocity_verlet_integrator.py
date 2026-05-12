import numpy as np


class VelocityVerletIntegrator:
    def __init__(self, x0, v0, accel_func):
        """
        Velocity-Verlet Integrator (Löser) für Differentialgleichungen
        der Form x''(t) = a(x(t), t)

        x0: Startposition (kann Skalar oder numpy-Array sein)
        v0: Startgeschwindigkeit
        accel_func: Eine Funktion a(x, t), die die Beschleunigung zurückgibt
        (rechte Seite der Differentialgleichung)
        """
        self.x = x0
        self.v = v0
        self.t = 0.0
        self.accel_func = accel_func

        # Speicher für Historie (optional für Plots)
        self.history_x = [x0]
        self.history_v = [v0]
        self.history_t = [0.0]

    def update(self, dt):
        """Führt einen Integrationsschritt mit Schrittweite dt aus."""

        ### 1. Update der Position: x(t) -> x(t+dt) bzw. x_n -> x_{n+1} ###
        # Berechne zunächst die aktuelle Beschleunigung: a(t) bzw. a_n:
        a_n = self.accel_func(self.x, self.t)
        # Update der Position:
        # x_{n+1} = x_n + v_n*dt + 0.5 * a_n * dt^2
        self.x += self.v * dt + 0.5 * a_n * dt**2
        # Update der Zeit (für zeitabhängige Beschleunigungen wichtig)
        self.t += dt

        ### 2. Update der Beschleunigung : a(t) -> a(t+dt) bzw. a_n -> a_{n+1} ###
        # a_{n+1} = a(x_{n+1}, t_{n+1})
        a_next = self.accel_func(self.x, self.t)

        ### 3. Update der Geschwindigkeit: v(t) -> v(t+dt) bzw. v_n -> v_{n+1} ###
        # v_{n+1} = v_n + 0.5 * (a_n + a_{n+1}) * dt
        self.v += 0.5 * (a_n + a_next) * dt

        # Historie speichern
        self.history_x.append(self.x)
        self.history_v.append(self.v)
        self.history_t.append(self.t)


# --- Beispiel für die Verwendung (Harmonischer Oszillator) ---
if __name__ == "__main__":
    # Beschleunigung: a(x, t) = -k * x
    # Differentialgleichung x''(t) = -k * x(t)
    k = 1.0

    def my_acceleration(x, t):
        return -k * x

    # Integrator instanziieren (Start bei x=1, v=0)
    sim = VelocityVerletIntegrator(x0=1.0, v0=0.0, accel_func=my_acceleration)

    # Simulation über 100 Schritte
    dt = 0.1
    for _ in range(100):
        sim.update(dt)

    print(
        f"Zeit: {sim.t:.2f} | Position x: {sim.x:.4f} | Geschwindigkeit v: {sim.v:.4f}"
    )
