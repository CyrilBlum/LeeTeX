from generate_correl_data import *
from adjustText import adjust_text
import matplotlib.pyplot as plt

plt.style.use("ggplot")


def visualize_normalized_data(df_correl, normalize=True, save=True, add_mean=True):
    if normalize:
        for column in df_correl.columns:
            # Normalize the data
            df_correl[column] = (
                df_correl[column] - df_correl[column].mean()
            )  # / df_correl[column].std()

    plt.figure(figsize=(8, 6))

    # Scatter plot with the same color for all dots
    plt.scatter(
        df_correl["Polizeistreifen"], df_correl["Straftaten"], color="purple", alpha=0.7
    )

    # Add data labels with arrows and rounded corners RoyalBlue box
    texts = []
    for i, (x, y) in enumerate(
        zip(df_correl["Polizeistreifen"], df_correl["Straftaten"])
    ):
        texts.append(
            plt.text(
                x + 0.1,
                y,  # Slightly shift labels to the right
                f"x'={x:.1f}\ny'={y:.1f}" if normalize else f"x={x:.1f}\ny={y:.1f}",
                fontsize=10,
                color="white",
                bbox=dict(
                    boxstyle="round,pad=0.3",
                    edgecolor="RoyalBlue",
                    facecolor="RoyalBlue",
                    alpha=0.5,  # Semi-transparent box
                ),
            )
        )

    # Adjust text positions to avoid overlap
    adjust_text(texts, arrowprops=dict(arrowstyle="->", color="gray", lw=0.5))

    # Get the actual plot limits
    x_min, x_max = plt.xlim()
    y_min, y_max = plt.ylim()

    if normalize:
        # Add horizontal and vertical lines at 0
        plt.axhline(0, color="black", linestyle="--", linewidth=1)
        plt.axvline(0, color="black", linestyle="--", linewidth=1)

        # Add background colors for each quadrant using actual plot limits
        plt.axhspan(
            0,
            y_max,
            xmin=(0 - x_min) / (x_max - x_min),
            xmax=x_max,
            facecolor="lightblue",
            alpha=0.3,
            label="Quadrant I",
        )
        plt.axhspan(
            0,
            y_max,
            xmin=0,
            xmax=(0 - x_min) / (x_max - x_min),
            facecolor="lightgreen",
            alpha=0.3,
            label="Quadrant II",
        )
        plt.axhspan(
            y_min,
            0,
            xmin=0,
            xmax=(0 - x_min) / (x_max - x_min),
            facecolor="lightcoral",
            alpha=0.3,
            label="Quadrant III",
        )
        plt.axhspan(
            y_min,
            0,
            xmin=(0 - x_min) / (x_max - x_min),
            xmax=x_max,
            facecolor="moccasin",
            alpha=0.3,
            label="Quadrant IV",
        )

    else:
        if add_mean:
            # Add horizontal and vertical lines at mean values
            plt.axhline(
                df_correl["Straftaten"].mean(),
                color="ForestGreen",
                linestyle="--",
                linewidth=1,
                label=f'$\overline{{y}}$={df_correl["Straftaten"].mean():.1f}',
            )
            plt.axvline(
                df_correl["Polizeistreifen"].mean(),
                color="RoyalBlue",
                linestyle="--",
                linewidth=1,
                label=f'$\overline{{x}}$={df_correl["Polizeistreifen"].mean():.1f}',
            )

    # Set x and y limits to the actual plot limits
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    # Add title, labels, grid, and legend
    plt.xlabel("Anzahl Polizeistreifen " + ("(=x)" if not normalize else "(=x')"))
    plt.ylabel("Anzahl Straftaten " + ("(=y)" if not normalize else "(=y')"))
    plt.grid(True)
    plt.legend()
    if save:
        plt.savefig(
            "Grundlagen_Info/10_KI_und_Algorithmen/Figures/polizei_vs_kriminalitaet_correl"
            + ("_norm" if normalize else "")
            + ("_mean" if add_mean and not normalize else "")
            + ".pdf",
            bbox_inches="tight",  # Remove white margins
        )  # Save the plot to a PDF file
        plt.close()
    else:
        plt.show()


if __name__ == "__main__":
    df_pol = generiere_korrelationsdaten("polizei_vs_kriminalitaet", n=20)
    df_pol.to_csv(
        "Grundlagen_Info/10_KI_und_Algorithmen/Code/polizei_vs_kriminalitaet.csv",
        index=False,
    )

    # visualize steps of adding mean and normalization
    visualize_normalized_data(df_pol, normalize=False, save=True, add_mean=False)
    visualize_normalized_data(df_pol, normalize=False, save=True, add_mean=True)
    visualize_normalized_data(df_pol, normalize=True, save=True, add_mean=False)

    # Korrelationskoeffizient manuell berechnen

    # Berechnung der Mittelwerte
    mean_x = df_pol["Polizeistreifen"].mean()
    mean_y = df_pol["Straftaten"].mean()

    # Berechnung des Korrelationskoeffizienten
    x_neu = df_pol["Polizeistreifen"] - mean_x
    y_neu = df_pol["Straftaten"] - mean_y
    zaehler = sum(x_neu * y_neu)

    teiler = (
        sum((df_pol["Polizeistreifen"] - mean_x) ** 2)
        * sum((df_pol["Straftaten"] - mean_y) ** 2)
    ) ** 0.5

    correlation_coefficient = zaehler / teiler
    print(
        f"Correlation Coefficient (calculated manually): {correlation_coefficient:.2f}, numerator: {zaehler:.2f}, denominator: {teiler:.2f}"
    )
