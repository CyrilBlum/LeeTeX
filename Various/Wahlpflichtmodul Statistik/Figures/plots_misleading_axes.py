import matplotlib.pyplot as plt
import numpy as np
import os

# ggplot Stil verwenden
plt.style.use('ggplot')

# Beispieldaten: Verkaufszahlen zweier Produkte
kategorien = ['Produkt A', 'Produkt B', 'Produkt C', 'Produkt D']
werte = [65, 70, 68, 72]

# Zwei Subplots nebeneinander erstellen
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Linkes Diagramm: Y-Achse startet bei 60 (IRREFÜHREND)
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
ax1.bar(kategorien, werte, color=colors, edgecolor='black')
ax1.set_ylim(60, 75)  # Y-Achse startet bei 60!
ax1.set_ylabel('Verkaufszahlen')
ax1.set_title('IRREFÜHREND: Y-Achse startet bei 60', fontweight='bold', color='red')
ax1.grid(True, alpha=0.3, axis='y')

# Rechtes Diagramm: Y-Achse startet bei 0 (KORREKT)
ax2.bar(kategorien, werte, color=colors, edgecolor='black')
ax2.set_ylim(0, 80)  # Y-Achse startet bei 0
ax2.set_ylabel('Verkaufszahlen')
ax2.set_title('KORREKT: Y-Achse startet bei 0', fontweight='bold', color='green')
ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout()

# Pfad zum Speicherort der Python-Datei ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'plots_misleading_axes.pdf')

# Als PDF exportieren
plt.savefig(output_path, format='pdf', bbox_inches='tight')
plt.close()

print(f"Vergleichsdiagramm wurde als {output_path} exportiert")
