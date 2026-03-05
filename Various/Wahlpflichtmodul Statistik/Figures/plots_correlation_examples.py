import matplotlib.pyplot as plt
import numpy as np
import os

# ggplot Stil verwenden
plt.style.use('ggplot')

# Drei Subplots für verschiedene Korrelationen
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

np.random.seed(42)
n = 100

# Plot 1: Positive Korrelation
x1 = np.random.uniform(0, 10, n)
y1 = 2 * x1 + np.random.normal(0, 2, n) + 5

ax1.scatter(x1, y1, alpha=0.6, s=50, color='#66b3ff', edgecolors='black', linewidth=0.5)
ax1.set_xlabel('Variable X', fontsize=11)
ax1.set_ylabel('Variable Y', fontsize=11)
ax1.set_title('Positive Korrelation\n(X steigt → Y steigt)', fontsize=12, fontweight='bold', color='green')
ax1.grid(True, alpha=0.3)

# Trendlinie hinzufügen
z1 = np.polyfit(x1, y1, 1)
p1 = np.poly1d(z1)
x_trend1 = np.linspace(x1.min(), x1.max(), 100)
ax1.plot(x_trend1, p1(x_trend1), 'r--', linewidth=2, alpha=0.7, label='Trend')
ax1.legend(fontsize=10)

# Plot 2: Negative Korrelation
x2 = np.random.uniform(0, 10, n)
y2 = -1.5 * x2 + np.random.normal(0, 2, n) + 20

ax2.scatter(x2, y2, alpha=0.6, s=50, color='#ff9999', edgecolors='black', linewidth=0.5)
ax2.set_xlabel('Variable X', fontsize=11)
ax2.set_ylabel('Variable Y', fontsize=11)
ax2.set_title('Negative Korrelation\n(X steigt → Y sinkt)', fontsize=12, fontweight='bold', color='red')
ax2.grid(True, alpha=0.3)

# Trendlinie hinzufügen
z2 = np.polyfit(x2, y2, 1)
p2 = np.poly1d(z2)
x_trend2 = np.linspace(x2.min(), x2.max(), 100)
ax2.plot(x_trend2, p2(x_trend2), 'b--', linewidth=2, alpha=0.7, label='Trend')
ax2.legend(fontsize=10)

# Plot 3: Keine Korrelation
x3 = np.random.uniform(0, 10, n)
y3 = np.random.normal(15, 3, n)

ax3.scatter(x3, y3, alpha=0.6, s=50, color='#99ff99', edgecolors='black', linewidth=0.5)
ax3.set_xlabel('Variable X', fontsize=11)
ax3.set_ylabel('Variable Y', fontsize=11)
ax3.set_title('Keine Korrelation\n(kein systematischer Zusammenhang)', fontsize=12, fontweight='bold', color='gray')
ax3.grid(True, alpha=0.3)

# Horizontale Linie beim Mittelwert
ax3.axhline(np.mean(y3), color='orange', linestyle='--', linewidth=2, alpha=0.7, label='Mittelwert Y')
ax3.legend(fontsize=10)

plt.tight_layout()

# Pfad zum Speicherort der Python-Datei ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'plots_correlation_examples.pdf')

# Als PDF exportieren
plt.savefig(output_path, format='pdf', bbox_inches='tight', transparent=True)
plt.close()

print(f"Korrelations-Beispiele wurden als {output_path} exportiert")
