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
labels = ['Mathematik', 'Deutsch', 'Englisch', 'Physik']

# Histogramm erstellen
fig, ax = plt.subplots(figsize=(10, 6))

# Histogramm für Deutsch
ax.hist(deutsch, bins=15, alpha=0.7, color='#66b3ff', edgecolor='black')

ax.set_ylabel('Häufigkeit')
ax.set_xlabel('Erreichte Punktzahl')
ax.set_title('Verteilung der Testergebnisse in Deutsch')
ax.grid(True, alpha=0.3, axis='y')

# Pfad zum Speicherort der Python-Datei ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'plots_histogram.pdf')

# Als PDF exportieren
plt.savefig(output_path, format='pdf', bbox_inches='tight')
plt.close()

print(f"Histogramm wurde als {output_path} exportiert")