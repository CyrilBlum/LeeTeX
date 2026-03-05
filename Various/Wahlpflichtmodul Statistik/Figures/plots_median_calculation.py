import matplotlib.pyplot as plt
import numpy as np
import os

# ggplot Stil verwenden
plt.style.use('ggplot')

# Die Daten aus der Aufgabe
data = np.array([20, 25, 25, 30, 30, 35, 40, 400])

# Mittelwert und Median berechnen
mean_val = np.mean(data)
median_val = np.median(data)

# Plot erstellen
fig, ax = plt.subplots(figsize=(14, 7))

# Datenpunkte auf einer Linie
y_position = 0.5
colors = ['#66b3ff'] * 7 + ['#ff6666']  # Ausreisser in rot

for i, val in enumerate(data):
    color = colors[i]
    size = 200 if val == 400 else 150
    ax.scatter(val, y_position, s=size, color=color, edgecolors='black', 
               linewidths=2, zorder=3, alpha=0.8)
#     ax.text(val, y_position - 0.15, f'{val} CHF', ha='center', va='top', 
        #     fontsize=11, fontweight='bold' if val == 400 else 'normal')

# Median-Markierung
ax.axvline(median_val, ymin=0.3, ymax=0.7, color='green', linestyle='-', 
           linewidth=4, label=f'Median = {median_val:.0f} CHF', zorder=2)

# Mittelwert-Markierung
ax.axvline(mean_val, ymin=0.3, ymax=0.7, color='red', linestyle='--', 
           linewidth=4, label=f'Mittelwert = {mean_val:.1f} CHF', zorder=2)

# Zusätzliche Erklärungen
# Median-Erklärung
ax.annotate('Median: Mittlerer Wert\nder sortierten Daten\n(robust gegen Ausreisser)', 
            xy=(median_val, 0.6), xytext=(median_val, 0.8),
            fontsize=11, ha='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.7', facecolor='lightgreen', alpha=0.8),
            arrowprops=dict(arrowstyle='->', lw=2.5, color='green'))

# Mittelwert-Erklärung
ax.annotate('Mittelwert: Arithmetisches Mittel\n605 ÷ 8 = 75.6 CHF\n(stark beeinflusst durch Ausreisser!)', 
            xy=(mean_val, 0.4), xytext=(mean_val, 0.15),
            fontsize=11, ha='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.7', facecolor='lightcoral', alpha=0.8),
            arrowprops=dict(arrowstyle='->', lw=2.5, color='red'))

# Ausreisser markieren
ax.annotate('Ausreisser!\nZieht Mittelwert\nstark nach rechts', 
            xy=(400, y_position), xytext=(350, 0.75),
            fontsize=11, ha='right', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.7', facecolor='yellow', alpha=0.9),
            arrowprops=dict(arrowstyle='->', lw=2.5, color='red'))

# Die beiden mittleren Werte (für Median) hervorheben
ax.plot([data[3], data[4]], [y_position, y_position], 
        color='green', linewidth=6, alpha=0.5, zorder=1)
ax.annotate('', xy=(data[3], y_position + 0.05), xytext=(data[4], y_position + 0.05),
            arrowprops=dict(arrowstyle='<->', lw=2.5, color='green'))
ax.text((data[3] + data[4]) / 2, y_position + 0.10, 
        'Median = (30+30)/2 = 30', 
        ha='center', fontsize=10, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='lightgreen', alpha=0.7))

ax.set_xlabel('Taschengeld (CHF)', fontsize=13, fontweight='bold')
ax.set_title('Median vs. Mittelwert: Einfluss von Ausreissern\nBeispiel: Monatliches Taschengeld in CHF', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_ylim(0, 1)
ax.set_xlim(-10, 430)
ax.set_yticks([])
ax.legend(loc='upper left', fontsize=12, framealpha=0.9)
# ax.grid(True, alpha=0.8, axis='x')

# Fazit-Box
textstr = 'FAZIT: Der Median (30 CHF) beschreibt\ndas "typische" Taschengeld besser,\nweil er robust gegen Ausreisser ist.'
props = dict(boxstyle='round', facecolor='lightblue', alpha=0.9, linewidth=2, edgecolor='darkblue')
ax.text(0.98, 0.05, textstr, transform=ax.transAxes, fontsize=11,
        verticalalignment='bottom', horizontalalignment='right', bbox=props, fontweight='bold')

plt.tight_layout()

# Pfad zum Speicherort der Python-Datei ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'plots_median_calculation.pdf')

# Als PDF exportieren
plt.savefig(output_path, format='pdf', bbox_inches='tight')
plt.close()

print(f"Median-Berechnung wurde als {output_path} exportiert")
