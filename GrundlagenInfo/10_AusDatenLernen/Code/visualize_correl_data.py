from generate_correl_data import *
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def vis_correl_data(df, x, y, file_name):
    # Daten visualisieren
    plt.scatter(df[x], df[y], alpha=0.7)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(True)
    plt.savefig("GrundlagenInfo/10_AusDatenLernen/Figures/"+file_name+".pdf", bbox_inches='tight')  # Save the plot to a PDF file with no white margins
    plt.tight_layout()
    plt.close()

# Visualize Polizei vs. Kriminalität
a = generiere_korrelationsdaten("polizei_vs_kriminalitaet", n=20)
vis_correl_data(a, "Polizeistreifen", "Straftaten", "polizei_vs_kriminalitaet")

# Visualize Social Media vs. Zufriedenheit
a = generiere_korrelationsdaten("socialmedia_vs_zufriedenheit")
vis_correl_data(a, "Beiträge pro Tag", "Zufriedenheit (0–10)", "socialmedia_vs_zufriedenheit")

# Visualize Haarlänge vs. Notenschnitt
df = generiere_korrelationsdaten("haarlaenge_vs_notenschnitt", n=14, seed=1)
vis_correl_data(df, "Haarlänge (cm)", "Notenschnitt", "haarlange_vs_notenschnitt")

# Visualize Schuhgrösse vs. Bücher
df = generiere_korrelationsdaten("schuhgroesse_vs_buecher", n=14, seed=1)
vis_correl_data(df, "Bücher gelesen", "Schuhgrösse", "buecher_vs_schuhgroesse")

# Visualize Berufserfahrung vs. Einladungswahrscheinlichkeit
df = generiere_korrelationsdaten("berufserfahrung_vs_einladung", n=14, seed=1)
vis_correl_data(df, "Berufsjahre", "Einladungswahrscheinlichkeit", "berufserfahrung_vs_einladung")
