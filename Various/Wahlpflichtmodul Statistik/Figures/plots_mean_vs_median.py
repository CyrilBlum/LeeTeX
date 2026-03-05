import matplotlib.pyplot as plt
import numpy as np
import os

# ggplot Stil verwenden
plt.style.use('ggplot')

# Zwei Subplots: symmetrisch und schief
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Symmetrische Verteilung
np.random.seed(42)
data_symmetric = np.random.normal(70, 8, 1000)

mean_sym = np.mean(data_symmetric)
median_sym = np.median(data_symmetric)

ax1.hist(data_symmetric, bins=30, alpha=0.7, color='#66b3ff', edgecolor='black')
ax1.axvline(mean_sym, color='red', linestyle='--', linewidth=2.5, label=f'Mittelwert = {mean_sym:.1f}')
ax1.axvline(median_sym, color='green', linestyle='-', linewidth=2.5, label=f'Median = {median_sym:.1f}')
ax1.set_xlabel('Werte', fontsize=11)
ax1.set_ylabel('Häufigkeit', fontsize=11)
ax1.set_title('Symmetrische Verteilung\n(Mittelwert ≈ Median)', fontsize=12, fontweight='bold')
ax1.legend(fontsize=10, loc='upper right')
ax1.grid(True, alpha=0.3, axis='y')

# Plot 2: Schiefe Verteilung mit Ausreissern
np.random.seed(43)
data_skewed = np.random.gamma(5, 2, 900)
# Ausreisser hinzufügen
outliers = np.array([45, 50, 55, 60, 65, 70, 75, 80, 85, 90])
data_skewed = np.concatenate([data_skewed, outliers])

mean_skewed = np.mean(data_skewed)
median_skewed = np.median(data_skewed)

ax2.hist(data_skewed, bins=40, alpha=0.7, color='#ff9999', edgecolor='black')
ax2.axvline(mean_skewed, color='red', linestyle='--', linewidth=2.5, label=f'Mittelwert = {mean_skewed:.1f}')
ax2.axvline(median_skewed, color='green', linestyle='-', linewidth=2.5, label=f'Median = {median_skewed:.1f}')
ax2.set_xlabel('Werte', fontsize=11)
ax2.set_ylabel('Häufigkeit', fontsize=11)
ax2.set_title('Schiefe Verteilung mit Ausreissern\n(Mittelwert > Median)', fontsize=12, fontweight='bold')
ax2.legend(fontsize=10, loc='upper right')
ax2.grid(True, alpha=0.3, axis='y')

# Annotation zur Erklärung
ax2.annotate('Ausreisser ziehen\nden Mittelwert\nnach rechts', 
             xy=(mean_skewed, 20), xytext=(mean_skewed + 15, 60),
             fontsize=10, ha='left',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.8),
             arrowprops=dict(arrowstyle='->', lw=2, color='red'))

plt.tight_layout()

# Pfad zum Speicherort der Python-Datei ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'plots_mean_vs_median.pdf')

# Als PDF exportieren
plt.savefig(output_path, format='pdf', bbox_inches='tight', transparent=True)
plt.close()

print(f"Mittelwert vs. Median Vergleich wurde als {output_path} exportiert")
