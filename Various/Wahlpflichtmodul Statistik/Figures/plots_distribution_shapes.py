import matplotlib.pyplot as plt
import numpy as np
import os

# ggplot Stil verwenden
plt.style.use('ggplot')

# 3x2 Subplots für verschiedene Verteilungsformen
fig, axes = plt.subplots(2, 3, figsize=(15, 9))
axes = axes.flatten()

np.random.seed(42)

# 1. Unimodal symmetrisch
data1 = np.random.normal(50, 10, 1000)
axes[0].hist(data1, bins=30, alpha=0.7, color='#66b3ff', edgecolor='black')
axes[0].axvline(np.mean(data1), color='red', linestyle='--', linewidth=2, label='Mittelwert')
axes[0].axvline(np.median(data1), color='green', linestyle='-', linewidth=2, label='Median')
axes[0].set_title('Unimodal & Symmetrisch', fontsize=11, fontweight='bold')
axes[0].set_ylabel('Häufigkeit', fontsize=10)
axes[0].legend(fontsize=8)
axes[0].grid(True, alpha=0.3, axis='y')

# 2. Unimodal rechtsschief (positive skew)
data2 = np.random.gamma(3, 2, 1000)
axes[1].hist(data2, bins=30, alpha=0.7, color='#ff9999', edgecolor='black')
axes[1].axvline(np.mean(data2), color='red', linestyle='--', linewidth=2, label='Mittelwert')
axes[1].axvline(np.median(data2), color='green', linestyle='-', linewidth=2, label='Median')
axes[1].set_title('Rechtsschief (positiv schief)\nMittelwert > Median', fontsize=11, fontweight='bold')
axes[1].legend(fontsize=8)
axes[1].grid(True, alpha=0.3, axis='y')

# 3. Unimodal linksschief (negative skew)
data3 = 100 - np.random.gamma(3, 2, 1000)
axes[2].hist(data3, bins=30, alpha=0.7, color='#99ff99', edgecolor='black')
axes[2].axvline(np.mean(data3), color='red', linestyle='--', linewidth=2, label='Mittelwert')
axes[2].axvline(np.median(data3), color='green', linestyle='-', linewidth=2, label='Median')
axes[2].set_title('Linksschief (negativ schief)\nMittelwert < Median', fontsize=11, fontweight='bold')
axes[2].legend(fontsize=8)
axes[2].grid(True, alpha=0.3, axis='y')

# 4. Bimodal
data4 = np.concatenate([np.random.normal(30, 5, 500), np.random.normal(60, 5, 500)])
axes[3].hist(data4, bins=35, alpha=0.7, color='#ffcc99', edgecolor='black')
axes[3].axvline(np.mean(data4), color='red', linestyle='--', linewidth=2, label='Mittelwert')
axes[3].axvline(np.median(data4), color='green', linestyle='-', linewidth=2, label='Median')
axes[3].set_title('Bimodal (zwei Gipfel)\nHinweis auf zwei Gruppen', fontsize=11, fontweight='bold')
axes[3].set_ylabel('Häufigkeit', fontsize=10)
axes[3].set_xlabel('Werte', fontsize=10)
axes[3].legend(fontsize=8)
axes[3].grid(True, alpha=0.3, axis='y')

# 5. Gleichverteilt (uniform)
data5 = np.random.uniform(20, 80, 1000)
axes[4].hist(data5, bins=30, alpha=0.7, color='#cc99ff', edgecolor='black')
axes[4].axvline(np.mean(data5), color='red', linestyle='--', linewidth=2, label='Mittelwert')
axes[4].axvline(np.median(data5), color='green', linestyle='-', linewidth=2, label='Median')
axes[4].set_title('Gleichverteilt (uniform)\nAlle Werte gleich häufig', fontsize=11, fontweight='bold')
axes[4].set_xlabel('Werte', fontsize=10)
axes[4].legend(fontsize=8)
axes[4].grid(True, alpha=0.3, axis='y')

# 6. Mit Ausreissern
data6_main = np.random.normal(50, 8, 950)
data6_outliers = np.array([10, 12, 90, 92, 95, 98] * 8 + [8, 100])
data6 = np.concatenate([data6_main, data6_outliers])
axes[5].hist(data6, bins=40, alpha=0.7, color='#ff99cc', edgecolor='black')
axes[5].axvline(np.mean(data6), color='red', linestyle='--', linewidth=2, label='Mittelwert')
axes[5].axvline(np.median(data6), color='green', linestyle='-', linewidth=2, label='Median')
axes[5].set_title('Mit Ausreissern\nMedian robuster als Mittelwert', fontsize=11, fontweight='bold')
axes[5].set_xlabel('Werte', fontsize=10)
axes[5].legend(fontsize=8)
axes[5].grid(True, alpha=0.3, axis='y')

# Beschriftung Ausreisser
axes[5].annotate('Ausreisser', xy=(10, 20), xytext=(20, 60),
                 fontsize=9, arrowprops=dict(arrowstyle='->', lw=1.5),
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))
axes[5].annotate('Ausreisser', xy=(95, 20), xytext=(75, 60),
                 fontsize=9, arrowprops=dict(arrowstyle='->', lw=1.5),
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))

plt.suptitle('Verschiedene Verteilungsformen', fontsize=14, fontweight='bold', y=0.995)
plt.tight_layout()

# Pfad zum Speicherort der Python-Datei ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'plots_distribution_shapes.pdf')

# Als PDF exportieren
plt.savefig(output_path, format='pdf', bbox_inches='tight', transparent=True)
plt.close()

print(f"Verteilungsformen wurden als {output_path} exportiert")
