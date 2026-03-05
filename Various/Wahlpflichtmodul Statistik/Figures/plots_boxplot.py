import matplotlib.pyplot as plt
import numpy as np
import os

# ggplot Stil verwenden
plt.style.use('ggplot')

# Beispieldaten: Testergebnisse (Punkte von 0-100) in verschiedenen Fächern
np.random.seed(42)
mathematik = np.random.normal(75, 12, 80)      # Durchschnitt 75, Streuung 12
deutsch = np.random.normal(68, 10, 80)         # Durchschnitt 68, Streuung 10
englisch = np.random.normal(72, 15, 80)        # Durchschnitt 72, Streuung 15
physik = np.random.normal(65, 14, 80)          # Durchschnitt 65, Streuung 14

data = [mathematik, deutsch, englisch, physik]

# Boxplot erstellen
fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot(data, labels=['Mathematik', 'Deutsch', 'Englisch', 'Physik'],
                patch_artist=True)

# Farben anpassen
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax.set_ylabel('Erreichte Punktzahl')
ax.set_xlabel('Fach')
ax.set_title('Vergleich der Testergebnisse nach Fächern')
ax.grid(True, alpha=0.3, axis='y')

# Pfad zum Speicherort der Python-Datei ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'plots_boxplot.pdf')

# Als PDF exportieren
plt.savefig(output_path, format='pdf', bbox_inches='tight')
plt.close()

print(f"Boxplot wurde als {output_path} exportiert")