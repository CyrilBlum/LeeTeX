import numpy as np
import pandas as pd
import os

# Seed für Reproduzierbarkeit
np.random.seed(42)

# Daten basierend auf der Kontingenztabelle aus dem Skript
# Mit Musik + Alleine: 45
# Mit Musik + Gruppe: 25
# Ohne Musik + Alleine: 35
# Ohne Musik + Gruppe: 55
# Total: 160

# Listen für jede Kombination erstellen
data_rows = []

# Mit Musik + Alleine: 45
for _ in range(45):
    data_rows.append({'Music': 'Mit Musik', 'StudyMode': 'Alleine'})

# Mit Musik + Gruppe: 25
for _ in range(25):
    data_rows.append({'Music': 'Mit Musik', 'StudyMode': 'Gruppe'})

# Ohne Musik + Alleine: 35
for _ in range(35):
    data_rows.append({'Music': 'Ohne Musik', 'StudyMode': 'Alleine'})

# Ohne Musik + Gruppe: 55
for _ in range(55):
    data_rows.append({'Music': 'Ohne Musik', 'StudyMode': 'Gruppe'})

# DataFrame erstellen
df = pd.DataFrame(data_rows)

# Daten mischen, damit sie nicht geordnet sind
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Optional: PersonID hinzufügen
df.insert(0, 'PersonID', range(1, len(df) + 1))

# Pfad zum Speicherort
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'music_study.csv')

# Als CSV speichern
df.to_csv(output_path, index=False)

print(f"Datensatz 'music_study.csv' wurde erstellt: {output_path}")
print(f"\nAnzahl Datenpunkte: {len(df)}")
print(f"\nKontingenztabelle (Häufigkeiten):")
contingency_table = pd.crosstab(df['Music'], df['StudyMode'], margins=True)
print(contingency_table)
print(f"\nKontingenztabelle (Prozente innerhalb StudyMode):")
contingency_pct = pd.crosstab(df['Music'], df['StudyMode'], normalize='columns') * 100
print(contingency_pct.round(1))
print(f"\nErste 10 Zeilen:")
print(df.head(10))
