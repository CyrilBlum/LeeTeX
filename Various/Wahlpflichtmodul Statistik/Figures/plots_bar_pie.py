import matplotlib.pyplot as plt
import os

# ggplot Stil verwenden
plt.style.use('ggplot')

# Beispieldaten: bevorzugtes Verkehrsmittel für den Schulweg
categories = ['Velo', 'Bus', 'Zu Fuss', 'Auto', 'Zug']
counts = [18, 26, 11, 8, 7]
colors = ['#66b3ff', '#99ff99', '#ffcc99', '#ff9999', '#c2c2f0']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Balkendiagramm
ax1.bar(categories, counts, color=colors, edgecolor='black')
ax1.set_xlabel('Kategorie')
ax1.set_ylabel('Anzahl Lernende')
ax1.set_title('Balkendiagramm: Schulweg nach Verkehrsmittel')
ax1.grid(True, axis='y', alpha=0.3)
ax1.set_ylim(0, max(counts) + 5)

# Kreisdiagramm
ax2.pie(
    counts,
    labels=categories,
    autopct='%1.0f%%',
    startangle=90,
    colors=colors,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1},
)
ax2.set_title('Kreisdiagramm: Anteile der Kategorien')
ax2.axis('equal')

plt.tight_layout()

# Pfad zum Speicherort der Python-Datei ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'plots_bar_pie.pdf')

# Als PDF exportieren
plt.savefig(output_path, format='pdf', bbox_inches='tight')
plt.close()

print(f"Balken- und Kreisdiagramm wurden als {output_path} exportiert")
