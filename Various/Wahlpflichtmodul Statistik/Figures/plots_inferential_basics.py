import os

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
np.random.seed(42)

fig, axes = plt.subplots(1, 3, figsize=(15, 4.8))

# Plot 1: Beobachteter Anteil vs. Zufallsverteilung
n = 40
p0 = 0.35
simulated_counts = np.random.binomial(n=n, p=p0, size=5000)
observed_count = 24

ax = axes[0]
ax.hist(simulated_counts, bins=np.arange(-0.5, n + 1.5, 1), color='#87c7ff', edgecolor='black', alpha=0.8)
ax.axvline(observed_count, color='crimson', linestyle='--', linewidth=2.2, label='Beobachtet: 24 von 40')
ax.set_title('Zufallsverteilung vs. Beobachtung', fontsize=11, fontweight='bold')
ax.set_xlabel('Anzahl Gähner in Gruppe')
ax.set_ylabel('Häufigkeit in Simulation')
ax.legend(fontsize=8)

# Plot 2: Effekt mit 95%-Vertrauensintervall
control_success = 14
exp_success = 24
n_group = 40

p_exp = exp_success / n_group
p_ctrl = control_success / n_group
diff = p_exp - p_ctrl
se = np.sqrt((p_exp * (1 - p_exp) / n_group) + (p_ctrl * (1 - p_ctrl) / n_group))
ci_low = diff - 1.96 * se
ci_high = diff + 1.96 * se

ax = axes[1]
ax.errorbar([0], [diff], yerr=[[diff - ci_low], [ci_high - diff]], fmt='o', color='darkgreen',
            ecolor='darkgreen', elinewidth=2, capsize=6, markersize=8)
ax.axhline(0, color='black', linestyle=':', linewidth=1.5)
ax.set_xlim(-0.8, 0.8)
ax.set_ylim(-0.15, 0.45)
ax.set_xticks([])
ax.set_ylabel('Differenz der Anteile\n(Experimental - Kontroll)')
ax.set_title('Effekt mit 95%-Vertrauensintervall', fontsize=11, fontweight='bold')
ax.text(0.02, ci_high + 0.02, f'95%-CI: [{ci_low:.2f}, {ci_high:.2f}]', fontsize=9)

# Plot 3: Kontrollgruppe vs. Experimentalgruppe
ax = axes[2]
labels = ['Kontrollgruppe', 'Experimentalgruppe']
rates = [p_ctrl, p_exp]
colors = ['#f4a261', '#2a9d8f']

bars = ax.bar(labels, rates, color=colors, edgecolor='black', alpha=0.85)
ax.set_ylim(0, 1)
ax.set_ylabel('Anteil gähnender Personen')
ax.set_title('Kontrollgruppe als Referenz', fontsize=11, fontweight='bold')

for bar, value in zip(bars, rates):
    ax.text(bar.get_x() + bar.get_width() / 2, value + 0.03, f'{value:.2f}', ha='center', fontsize=9)

plt.suptitle('Schliessende Statistik: Zufall, Intervall, Vergleich', fontsize=14, fontweight='bold')
plt.tight_layout()

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'plots_inferential_basics.pdf')

plt.savefig(output_path, format='pdf', bbox_inches='tight', transparent=True)
plt.close()

print(f'Grafik exportiert nach: {output_path}')
