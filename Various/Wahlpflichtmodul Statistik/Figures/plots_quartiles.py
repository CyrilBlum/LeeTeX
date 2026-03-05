import matplotlib.pyplot as plt
import numpy as np
import os

# ggplot Stil verwenden
plt.style.use('ggplot')

# Beispieldaten
np.random.seed(42)
data = np.array([12, 15, 18, 20, 22, 25, 28, 30, 32, 35, 38, 40, 42, 45, 48, 50, 52, 55, 58, 60])
data_sorted = np.sort(data)

# Quartile berechnen
q1 = np.percentile(data_sorted, 25)
q2 = np.percentile(data_sorted, 50)  # Median
q3 = np.percentile(data_sorted, 75)

# Plot erstellen
fig, ax = plt.subplots(figsize=(14, 8))

# Daten als Punkte auf einer Linie darstellen
y_position = 0.5
ax.scatter(data_sorted, [y_position] * len(data_sorted), s=100, color='#66b3ff', 
           edgecolors='black', linewidths=1.5, zorder=3, alpha=0.8)

# Zahlen unter den Punkten
for i, val in enumerate(data_sorted):
    ax.text(val, y_position - 0.08, str(val), ha='center', va='top', fontsize=9)

# Quartil-Linien
line_height = 0.15
ax.axvline(q1, ymin=0.3, ymax=0.7, color='orange', linestyle='--', linewidth=3, label=f'Q1 = {q1:.0f}')
ax.axvline(q2, ymin=0.3, ymax=0.7, color='green', linestyle='-', linewidth=3, label=f'Q2 (Median) = {q2:.0f}')
ax.axvline(q3, ymin=0.3, ymax=0.7, color='orange', linestyle='--', linewidth=3, label=f'Q3 = {q3:.0f}')

# Bereiche markieren
y_label = 0.75
colors_light = ['#ffcccc', '#ccffcc', '#ccccff', '#ffffcc']
labels = ['25% der Daten\n(1. Quartil)', '25% der Daten\n(2. Quartil)', 
          '25% der Daten\n(3. Quartil)', '25% der Daten\n(4. Quartil)']

# Bereich 1: Min bis Q1
ax.fill_betweenx([y_label - 0.05, y_label + 0.05], data_sorted.min(), q1, 
                  color=colors_light[0], alpha=0.6, zorder=1)
ax.text((data_sorted.min() + q1) / 2, y_label, labels[0], 
        ha='center', va='center', fontsize=10, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))

# Bereich 2: Q1 bis Q2
ax.fill_betweenx([y_label - 0.05, y_label + 0.05], q1, q2, 
                  color=colors_light[1], alpha=0.6, zorder=1)
ax.text((q1 + q2) / 2, y_label, labels[1], 
        ha='center', va='center', fontsize=10, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))

# Bereich 3: Q2 bis Q3
ax.fill_betweenx([y_label - 0.05, y_label + 0.05], q2, q3, 
                  color=colors_light[2], alpha=0.6, zorder=1)
ax.text((q2 + q3) / 2, y_label, labels[2], 
        ha='center', va='center', fontsize=10, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))

# Bereich 4: Q3 bis Max
ax.fill_betweenx([y_label - 0.05, y_label + 0.05], q3, data_sorted.max(), 
                  color=colors_light[3], alpha=0.6, zorder=1)
ax.text((q3 + data_sorted.max()) / 2, y_label, labels[3], 
        ha='center', va='center', fontsize=10, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))

# IQR Markierung
ax.annotate('', xy=(q1, 0.25), xytext=(q3, 0.25),
            arrowprops=dict(arrowstyle='<->', lw=2.5, color='red'))
ax.text((q1 + q3) / 2, 0.2, f'IQR = Q3 - Q1 = {q3:.0f} - {q1:.0f} = {q3-q1:.0f}', 
        ha='center', va='top', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.8))

ax.set_xlabel('Werte', fontsize=12, fontweight='bold')
ax.set_title('Quartile: Einteilung der Daten in vier gleich grosse Teile', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_ylim(0.1, 0.9)
ax.set_yticks([])
ax.legend(loc='upper right', fontsize=11)
ax.grid(True, alpha=0.3, axis='x')

plt.tight_layout()

# Pfad zum Speicherort der Python-Datei ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'plots_quartiles.pdf')

# Als PDF exportieren
plt.savefig(output_path, format='pdf', bbox_inches='tight', transparent=True)
plt.close()

print(f"Quartile-Illustration wurde als {output_path} exportiert")
