from generate_correl_data import *
import matplotlib.pyplot as plt

plt.style.use("ggplot")


def vis_correl_data(df, x, y, file_name):
    # Daten visualisieren
    plt.scatter(df[x], df[y], alpha=0.7)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(True)
    plt.savefig(
        "Grundlagen_Info/10_KI_und_Algorithmen/Figures/" + file_name + ".pdf",
        bbox_inches="tight",
    )  # Save the plot to a PDF file with no white margins
    plt.tight_layout()
    plt.close()


if __name__ == "__main__":
    # Visualize Polizei vs. Kriminalität
    a = generiere_korrelationsdaten("polizei_vs_kriminalitaet", n=20)
    vis_correl_data(a, "Polizeistreifen", "Straftaten", "polizei_vs_kriminalitaet")

    # Visualize Social Media vs. Zufriedenheit
    a = generiere_korrelationsdaten("socialmedia_vs_zufriedenheit")
    vis_correl_data(
        a, "Beiträge pro Tag", "Zufriedenheit (0–10)", "socialmedia_vs_zufriedenheit"
    )

    # Visualize Haarlänge vs. Note
    df = generiere_korrelationsdaten("haarlaenge_vs_note", n=14, seed=1)
    vis_correl_data(df, "Haarlänge (cm)", "Note", "haarlange_vs_note")

    # Visualize Schuhgrösse vs. Bücher
    df = generiere_korrelationsdaten("schuhgroesse_vs_buecher", n=14, seed=1)
    vis_correl_data(df, "Bücher gelesen", "Schuhgrösse", "buecher_vs_schuhgroesse")

    # Visualize Berufserfahrung vs. Einladungswahrscheinlichkeit
    df = generiere_korrelationsdaten("berufserfahrung_vs_einladung", n=14, seed=1)
    vis_correl_data(
        df,
        "Berufsjahre",
        "Einladungswahrscheinlichkeit",
        "berufserfahrung_vs_einladung",
    )

    # Visualize Schlafdauer vs. Note
    df = generiere_korrelationsdaten("schlafdauer_vs_note", n=25)
    vis_correl_data(df, "Schlafdauer", "Note", "schlafdauer_vs_note")
