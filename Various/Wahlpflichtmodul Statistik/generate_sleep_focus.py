import numpy as np
import pandas as pd
import os

# Seed für Reproduzierbarkeit
np.random.seed(42)

# Anzahl Datenpunkte
n = 100

# 1. SleepHours: Schlafdauer in Stunden (realistisch: 4-10 Stunden, Durchschnitt ~7h)
sleep_hours = np.random.normal(7.0, 1.2, n)
sleep_hours = np.clip(sleep_hours, 3.5, 10.5)  # Realistische Grenzen

# 2. PhoneMinutes: Smartphone-Nutzung in Minuten
# Normalverteilung mit einigen Ausreissern
phone_base = np.random.gamma(8, 15, n)  # Rechtsschief verteilt
# Einige Ausreisser hinzufügen (Heavy Users)
outlier_indices = np.random.choice(n, size=8, replace=False)
phone_base[outlier_indices] = np.random.uniform(280, 350, 8)
phone_minutes = np.clip(phone_base, 20, 400).astype(int)

# 3. Coffee: Kaffeekonsum (0-4, ordinal)
coffee = np.random.choice([0, 1, 2, 3, 4], n, p=[0.1, 0.25, 0.35, 0.2, 0.1])

# 4. Stress: Stresslevel (1-5, ordinal)
stress = np.random.choice([1, 2, 3, 4, 5], n, p=[0.1, 0.2, 0.35, 0.25, 0.1])

# 5. FocusScore: Fokus-Score (0-100)
# Positive Korrelation mit Schlaf, negative mit Stress und Phone
# Formel: Basis + positive Effekte - negative Effekte + Rauschen
base_focus = 50
focus_score = (
    base_focus 
    + (sleep_hours - 7) * 5  # +5 Punkte pro Stunde mehr Schlaf
    - (stress - 3) * 4        # -4 Punkte pro Stresslevel über 3
    - (phone_minutes - 150) / 30  # Smartphone-Effekt
    + np.random.normal(0, 8, n)  # Rauschen
)
focus_score = np.clip(focus_score, 0, 100).astype(int)

# DataFrame erstellen
df = pd.DataFrame({
    'SleepHours': np.round(sleep_hours, 1),
    'PhoneMinutes': phone_minutes,
    'Coffee': coffee,
    'Stress': stress,
    'FocusScore': focus_score
})

# Pfad zum Speicherort
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'sleep_focus.csv')

# Als CSV speichern
df.to_csv(output_path, index=False)

print(f"Datensatz 'sleep_focus.csv' wurde erstellt: {output_path}")
print(f"\nStatistiken:")
print(f"Anzahl Datenpunkte: {len(df)}")
print(f"\nSleepHours:")
print(f"  Mittelwert: {df['SleepHours'].mean():.2f}")
print(f"  Median: {df['SleepHours'].median():.2f}")
print(f"  Min-Max: {df['SleepHours'].min():.1f} - {df['SleepHours'].max():.1f}")
print(f"\nPhoneMinutes:")
print(f"  Mittelwert: {df['PhoneMinutes'].mean():.1f}")
print(f"  Median: {df['PhoneMinutes'].median():.1f}")
print(f"  Ausreisser (>280): {(df['PhoneMinutes'] > 280).sum()}")
print(f"\nFocusScore:")
print(f"  Mittelwert: {df['FocusScore'].mean():.1f}")
print(f"  Median: {df['FocusScore'].median():.1f}")
print(f"  Korrelation mit SleepHours: {df['SleepHours'].corr(df['FocusScore']):.3f}")
print(f"\nErste 5 Zeilen:")
print(df.head())
