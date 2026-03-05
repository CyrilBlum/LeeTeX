import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import os

# ggplot Stil verwenden
plt.style.use('ggplot')

# Normalverteilung erstellen
mu = 70  # Mittelwert
sigma = 10  # Standardabweichung
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Plot erstellen
fig, ax = plt.subplots(figsize=(12, 7))

# Grundkurve
ax.plot(x, y, 'b-', linewidth=2.5, label='Normalverteilung')

# Bereiche färben
# ±1 Standardabweichung (ca. 68%)
x1 = x[(x >= mu - sigma) & (x <= mu + sigma)]
y1 = norm.pdf(x1, mu, sigma)
ax.fill_between(x1, y1, alpha=0.5, color='#66b3ff', label='±1 SD (~68%)')

# ±2 Standardabweichungen (ca. 95%)
x2_left = x[(x >= mu - 2*sigma) & (x < mu - sigma)]
x2_right = x[(x > mu + sigma) & (x <= mu + 2*sigma)]
y2_left = norm.pdf(x2_left, mu, sigma)
y2_right = norm.pdf(x2_right, mu, sigma)
ax.fill_between(x2_left, y2_left, alpha=0.4, color='#99ccff', label='±2 SD (~95%)')
ax.fill_between(x2_right, y2_right, alpha=0.4, color='#99ccff')

# ±3 Standardabweichungen (ca. 99.7%)
x3_left = x[(x >= mu - 3*sigma) & (x < mu - 2*sigma)]
x3_right = x[(x > mu + 2*sigma) & (x <= mu + 3*sigma)]
y3_left = norm.pdf(x3_left, mu, sigma)
y3_right = norm.pdf(x3_right, mu, sigma)
ax.fill_between(x3_left, y3_left, alpha=0.3, color='#cce5ff', label='±3 SD (~99.7%)')
ax.fill_between(x3_right, y3_right, alpha=0.3, color='#cce5ff')

# Vertikale Linien für Mittelwert und Standardabweichungen
ax.axvline(mu, color='red', linestyle='-', linewidth=2.5, label=f'Mittelwert μ = {mu}')
ax.axvline(mu - sigma, color='orange', linestyle='--', linewidth=2)
ax.axvline(mu + sigma, color='orange', linestyle='--', linewidth=2)
ax.axvline(mu - 2*sigma, color='green', linestyle='--', linewidth=1.5)
ax.axvline(mu + 2*sigma, color='green', linestyle='--', linewidth=1.5)
ax.axvline(mu - 3*sigma, color='purple', linestyle='--', linewidth=1)
ax.axvline(mu + 3*sigma, color='purple', linestyle='--', linewidth=1)

# Beschriftungen bei den wichtigen Punkten
offset_y = 0.042
ax.text(mu, offset_y, f'μ\n{mu}', ha='center', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='red', alpha=0.3))

ax.text(mu - sigma, offset_y - 0.002, f'μ-σ\n{mu-sigma}', ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='orange', alpha=0.3))
ax.text(mu + sigma, offset_y - 0.002, f'μ+σ\n{mu+sigma}', ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='orange', alpha=0.3))

ax.text(mu - 2*sigma, offset_y - 0.004, f'μ-2σ\n{mu-2*sigma}', ha='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.3))
ax.text(mu + 2*sigma, offset_y - 0.004, f'μ+2σ\n{mu+2*sigma}', ha='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.3))

# Prozentangaben in den Bereichen
ax.text(mu, 0.025, '68.3%', ha='center', fontsize=12, fontweight='bold', color='darkblue')
ax.text(mu - 1.5*sigma, 0.015, '13.6%', ha='center', fontsize=11, color='darkblue')
ax.text(mu + 1.5*sigma, 0.015, '13.6%', ha='center', fontsize=11, color='darkblue')
ax.text(mu - 2.5*sigma, 0.007, '2.1%', ha='center', fontsize=10, color='darkblue')
ax.text(mu + 2.5*sigma, 0.007, '2.1%', ha='center', fontsize=10, color='darkblue')

ax.set_xlabel('Werte', fontsize=12, fontweight='bold')
ax.set_ylabel('Wahrscheinlichkeitsdichte', fontsize=12, fontweight='bold')
ax.set_title('Standardabweichung (σ): Streuung um den Mittelwert\nEmpirische Regel bei Normalverteilung', 
             fontsize=13, fontweight='bold', pad=15)
ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3, axis='y')
ax.set_xlim(30, 110)

# Zusätzliche Erklärung
textstr = 'Standardabweichung (SD) misst,\nwie weit Werte typischerweise\nvom Mittelwert entfernt sind.'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.7)
ax.text(0.02, 0.97, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

plt.tight_layout()

# Pfad zum Speicherort der Python-Datei ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'plots_standard_deviation.pdf')

# Als PDF exportieren
plt.savefig(output_path, format='pdf', bbox_inches='tight', transparent=True)
plt.close()

print(f"Standardabweichung-Visualisierung wurde als {output_path} exportiert")
