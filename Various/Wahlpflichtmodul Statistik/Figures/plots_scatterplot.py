import csv
import matplotlib.pyplot as plt
import numpy as np
import os

# ggplot Stil verwenden
plt.style.use('ggplot')

# Datensatz laden (SleepHours vs. FocusScore)
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, '..', 'sleep_focus.csv')

sleep_hours = []
focus_score = []

with open(data_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sleep_hours.append(float(row['SleepHours']))
        focus_score.append(float(row['FocusScore']))

sleep_hours = np.array(sleep_hours)
focus_score = np.array(focus_score)

fig, ax = plt.subplots(figsize=(8, 6))

# Scatterplot
ax.scatter(
    sleep_hours,
    focus_score,
    alpha=0.75,
    s=55,
    color='#66b3ff',
    edgecolors='black',
    linewidth=0.5,
)

# Trendlinie
coef = np.polyfit(sleep_hours, focus_score, 1)
trend = np.poly1d(coef)
x_fit = np.linspace(sleep_hours.min(), sleep_hours.max(), 100)
ax.plot(x_fit, trend(x_fit), color='#d62728', linestyle='--', linewidth=2, label='Trendlinie')

ax.set_xlabel('Schlafdauer (Stunden)')
ax.set_ylabel('Fokus-Score (0-100)')
ax.set_title('Scatterplot: Schlafdauer und Fokus')
ax.grid(True, alpha=0.3)
ax.legend()

plt.tight_layout()

output_path = os.path.join(script_dir, 'plots_scatterplot.pdf')

# Als PDF exportieren
plt.savefig(output_path, format='pdf', bbox_inches='tight')
plt.close()

print(f"Scatterplot wurde als {output_path} exportiert")
