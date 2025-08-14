import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def max_kaufpreis(E, b):
    """
    Berechnet den maximalen Kaufpreis k basierend auf Eigenkapital E
    und Bruttolohn b.
    """
    k0 = (100 * b + 15 * E) / 18
    k1 = 150 * b / 37 + 105 * E / 74
    k = np.minimum(np.minimum(k0, k1), 5 * E)
    return np.maximum(k, E)

# --- 3D-Plot: k vs. E und b ---
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Definieren der Wertebereiche für E und b
# E_mesh, b_mesh = np.meshgrid(np.linspace(0, 500000, 50), np.linspace(0, 10000, 50))
E_mesh, b_mesh = np.meshgrid(np.linspace(0, 2000, 80), np.linspace(0, 350, 80))

# Berechnung der k-Werte für jedes (E, b) Paar
k_mesh = max_kaufpreis(E_mesh, b_mesh)

# Erstellen der 3D-Oberfläche
ax.plot_surface(E_mesh, b_mesh, k_mesh, cmap='viridis')

# Beschriftungen und Titel festlegen
ax.set_title('3D-Plot: Maximaler Kaufpreis k(E, b)')
ax.set_xlabel('Eigenkapital (E) in CHF')
ax.set_ylabel('Bruttolohn (b) in CHF')
ax.set_zlabel('Maximaler Kaufpreis (k) in CHF')

plt.show()