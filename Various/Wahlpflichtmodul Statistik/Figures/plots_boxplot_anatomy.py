import matplotlib.pyplot as plt
import numpy as np
import os

# ggplot Stil verwenden
plt.style.use('ggplot')

# Beispieldaten für Boxplot
np.random.seed(42)
data = np.random.normal(70, 10, 100)
# Einige Ausreisser hinzufügen
data = np.append(data, [95, 98, 35, 32])

# Quartile berechnen
q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)  # Median
q3 = np.percentile(data, 75)
iqr = q3 - q1
whisker_low = q1 - 1.5 * iqr
whisker_high = q3 + 1.5 * iqr

# Tatsächliche Whisker-Positionen
actual_whisker_low = data[data >= whisker_low].min()
actual_whisker_high = data[data <= whisker_high].max()

# Ausreisser
outliers = data[(data < whisker_low) | (data > whisker_high)]

# Plot erstellen
fig, ax = plt.subplots(figsize=(10, 8))

# Boxplot erstellen
bp = ax.boxplot([data], vert=True, widths=0.5, patch_artist=True,
                showfliers=True, labels=[''])

# Farbe anpassen
bp['boxes'][0].set_facecolor('#66b3ff')
bp['boxes'][0].set_alpha(0.7)

# Beschriftungen hinzufügen
offset = 0.15

# Q1
ax.annotate(f'Q1 (25% Quantil)\n= {q1:.1f}', 
            xy=(1, q1), xytext=(1 + offset, q1),
            fontsize=11, ha='left',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
            arrowprops=dict(arrowstyle='->', lw=1.5))

# Median
ax.annotate(f'Median (Q2)\n= {q2:.1f}', 
            xy=(1, q2), xytext=(1 + offset, q2 + 3),
            fontsize=11, ha='left', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.8),
            arrowprops=dict(arrowstyle='->', lw=2))

# Q3
ax.annotate(f'Q3 (75% Quantil)\n= {q3:.1f}', 
            xy=(1, q3), xytext=(1 + offset, q3),
            fontsize=11, ha='left',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
            arrowprops=dict(arrowstyle='->', lw=1.5))

# IQR
ax.annotate('', xy=(0.65, q1), xytext=(0.65, q3),
            arrowprops=dict(arrowstyle='<->', lw=2, color='red'))
ax.text(0.55, (q1 + q3) / 2, f'IQR\n= {iqr:.1f}', 
        fontsize=11, ha='right', va='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.7))

# Unterer Whisker
ax.annotate(f'Unterer Whisker\n(kleinster Wert ≥ Q1-1.5×IQR)', 
            xy=(1, actual_whisker_low), xytext=(1 - offset - 0.1, actual_whisker_low - 8),
            fontsize=10, ha='right',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.7),
            arrowprops=dict(arrowstyle='->', lw=1.5))

# Oberer Whisker
ax.annotate(f'Oberer Whisker\n(grösster Wert ≤ Q3+1.5×IQR)', 
            xy=(1, actual_whisker_high), xytext=(1 - offset - 0.1, actual_whisker_high + 8),
            fontsize=10, ha='right',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.7),
            arrowprops=dict(arrowstyle='->', lw=1.5))

# Ausreisser
ax.annotate(f'Ausreisser\n(> Q3+1.5×IQR)', 
            xy=(1, outliers[outliers > whisker_high].mean()), 
            xytext=(1 + offset + 0.05, 96),
            fontsize=10, ha='left',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='orange', alpha=0.7),
            arrowprops=dict(arrowstyle='->', lw=1.5))

ax.annotate(f'Ausreisser\n(< Q1-1.5×IQR)', 
            xy=(1, outliers[outliers < whisker_low].mean()), 
            xytext=(1 + offset + 0.05, 33),
            fontsize=10, ha='left',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='orange', alpha=0.7),
            arrowprops=dict(arrowstyle='->', lw=1.5))

ax.set_ylabel('Werte', fontsize=12)
ax.set_title('Anatomie eines Boxplots', fontsize=14, fontweight='bold')
ax.set_xlim(0.4, 1.6)
ax.set_xticks([])
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()

# Pfad zum Speicherort der Python-Datei ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'plots_boxplot_anatomy.pdf')

# Als PDF exportieren
plt.savefig(output_path, format='pdf', bbox_inches='tight', transparent=True)
plt.close()

print(f"Boxplot-Anatomie wurde als {output_path} exportiert")
