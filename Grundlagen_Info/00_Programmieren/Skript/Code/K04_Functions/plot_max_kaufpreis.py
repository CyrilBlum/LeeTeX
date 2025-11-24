import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from max_kaufpreis import max_kaufpreis


def plot_2d_max_kaufpreis(alpha, beta):
    """
    Erstellt einen 2D-Plot des maximalen Kaufpreises vs. Eigenkapital
    für verschiedene Bruttolöhne.
    """
    # Definieren Sie verschiedene Bruttolohnwerte b, die wir plotten möchten
    b_values_to_plot = [
        0,
        2,
        4,
        5,
        10,
        20,
        30,
        40,
        60,
        80,
        100,
        130,
        160,
        190,
        220,
        250,
        280,
        300,
    ]  # Beispielwerte in 1000 CHF

    # Erzeugen eines Wertebereichs für das Eigenkapital E
    E_values = np.linspace(0, 1000, 200)  # Werte in 1000 CHF für eine glattere Kurve

    # Erstellen des Plots mit einer besseren Größe
    plt.figure(figsize=(12, 8))

    # Wählen Sie eine ansprechende Farbpalette
    colors = plt.cm.plasma(np.linspace(0, 1, len(b_values_to_plot)))

    # Iterieren Sie durch die b-Werte und plotten Sie eine Linie für jeden
    for i, b_value in enumerate(b_values_to_plot):
        k_values = max_kaufpreis(E_values, b_value, alpha, beta)
        plt.plot(
            E_values,
            k_values,
            label=f"Bruttolohn = {b_value} (in 1000 CHF)",
            color=colors[i],
            linewidth=1.5,
        )

    plt.xlabel("Eigenkapital (in 1000 CHF)", fontsize=12, fontweight="bold")
    plt.ylabel("Maximaler Kaufpreis (in 1000 CHF)", fontsize=12, fontweight="bold")
    plt.title(
        "Maximaler Kaufpreis in Abhängigkeit vom Eigenkapital für verschiedene Bruttolöhne",
        fontsize=14,
        fontweight="bold",
    )
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(title="Legende", loc="upper left")
    plt.tight_layout()  # Verbessert die Platzierung der Elemente

    # Speichert den Plot als Datei im aktuellen Verzeichnis
    plt.savefig(
        "Grundlagen_Info/00_Programmieren/Skript/Code/K04_Functions/max_kaufpreis_2d_plot.pdf"
    )

    plt.show()


def plot_3d_max_kaufpreis(alpha, beta):
    """
    Erstellt einen 3D-Plot des maximalen Kaufpreises in Abhängigkeit von
    Eigenkapital und Bruttolohn.
    """
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection="3d")

    # Definieren der Wertebereiche für E und b
    E_mesh, b_mesh = np.meshgrid(np.linspace(0, 2000, 100), np.linspace(0, 350, 100))

    # Berechnung der k-Werte für jedes (E, b) Paar
    k_mesh = max_kaufpreis(E_mesh, b_mesh, alpha, beta)

    # Erstellen der 3D-Oberfläche mit ansprechenderen Einstellungen
    surf = ax.plot_surface(
        E_mesh,
        b_mesh,
        k_mesh,
        cmap="viridis",
        rstride=1,
        cstride=1,
        alpha=0.9,
        edgecolor="none",
    )

    # Beschriftungen und Titel festlegen
    ax.set_title(
        "Maximaler Kaufpreis (in 1000 CHF) in Abhängigkeit von Eigenkapital und Bruttolohn",
        fontsize=14,
        fontweight="bold",
    )
    ax.set_xlabel("Eigenkapital (in 1000 CHF)", fontsize=12)
    ax.set_ylabel("Bruttolohn (in 1000 CHF)", fontsize=12)
    ax.set_zlabel("Maximaler Kaufpreis (in 1000 CHF)", fontsize=12)

    # Farbleiste hinzufügen
    fig.colorbar(surf, shrink=0.5, aspect=10, label="Maximaler Kaufpreis")

    # Blickwinkel anpassen, um die Oberfläche besser zu sehen
    ax.view_init(elev=30, azim=135)  # elev=Höhe, azim=Winkel

    # Speichert den Plot als Datei im aktuellen Verzeichnis
    plt.savefig(
        "Grundlagen_Info/00_Programmieren/Skript/Code/K04_Functions/max_kaufpreis_3d_plot.pdf"
    )

    plt.show()


# Rufen Sie die Funktionen auf, um die Plots zu erstellen
plot_2d_max_kaufpreis(0.05, 0.01)
plot_3d_max_kaufpreis(0.05, 0.01)
