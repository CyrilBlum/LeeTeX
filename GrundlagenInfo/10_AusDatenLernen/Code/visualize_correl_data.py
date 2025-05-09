from generate_correl_data import *
import matplotlib.pyplot as plt

a = generiere_korrelationsdaten("polizei_vs_kriminalitaet", n=20)


# Daten visualisieren
plt.scatter(a["Polizeistreifen"], a["Straftaten"], alpha=0.7)
plt.title("Polizeistreifen vs. Straftaten")
plt.xlabel("Polizeistreifen")
plt.ylabel("Straftaten")
plt.grid(True)
plt.savefig("GrundlagenInfo/10_AusDatenLernen/Figures/polizei_vs_kriminalitaet.pdf")  # Save the plot to a PDF file
plt.show()

# Visualize the second dataset
a = generiere_korrelationsdaten("socialmedia_vs_zufriedenheit")

plt.scatter(a["Beiträge pro Tag"], a["Zufriedenheit (0–10)"], alpha=0.7)
plt.title("Social-Media-Nutzung vs. Zufriedenheit")
plt.xlabel("Social-Media-Nutzung (Stunden pro Tag)")
plt.ylabel("Zufriedenheit (1-10)")
plt.grid(True)
plt.savefig("GrundlagenInfo/10_AusDatenLernen/Figures/socialmedia_vs_zufriedenheit.pdf")  # Save the plot to a PDF file
plt.show()
