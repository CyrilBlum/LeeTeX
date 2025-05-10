from generate_correl_data import *
from adjustText import adjust_text
import matplotlib.pyplot as plt

a = generiere_korrelationsdaten("polizei_vs_kriminalitaet", n=20)
a.to_csv("GrundlagenInfo/10_AusDatenLernen/Code/polizei_vs_kriminalitaet.csv", index=False)

# Describe each column with statistics using .describe()
print("Column Statistics:")
print(a.describe())

print(a)
# normalize and standardize 'a'
a_diff = a.copy()
for column in a.columns:
    # calculate difference from mean
    a_diff[column] = (a_diff[column] - a_diff[column].mean())

print(a_diff)


def visualize_normalized_data(a_diff):
    plt.figure(figsize=(8, 6))

    # Scatter plot with the same color for all dots
    plt.scatter(a_diff["Polizeistreifen"], a_diff["Straftaten"], color='purple', alpha=0.7)

    # Add horizontal and vertical lines at 0
    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.axvline(0, color='black', linestyle='--', linewidth=1)

    # Add data labels with arrows and rounded corners RoyalBlue box
    texts = []
    for i, (x, y) in enumerate(zip(a_diff["Polizeistreifen"], a_diff["Straftaten"])):
        texts.append(
            plt.text(
                x + 0.1, y,  # Slightly shift labels to the right
                f"x={x:.2f}\ny={y:.2f}",
                fontsize=8,
                color='white',
                bbox=dict(
                    boxstyle="round,pad=0.3",
                    edgecolor='RoyalBlue',
                    facecolor='RoyalBlue',
                    alpha=0.5  # Semi-transparent box
                )
            )
        )

    # Adjust text positions to avoid overlap
    adjust_text(texts, arrowprops=dict(arrowstyle="->", color='gray', lw=0.5))

    # Get the actual plot limits
    x_min, x_max = plt.xlim()
    y_min, y_max = plt.ylim()

    # Add background colors for each quadrant using actual plot limits
    plt.axhspan(0, y_max, xmin=0, xmax=(0 - x_min) / (x_max - x_min), facecolor='lightblue', alpha=0.3, label='Quadrant I')
    plt.axhspan(0, y_max, xmin=(0 - x_min) / (x_max - x_min), xmax=x_max, facecolor='lightgreen', alpha=0.3, label='Quadrant II')
    plt.axhspan(y_min, 0, xmin=0, xmax=(0 - x_min) / (x_max - x_min), facecolor='lightcoral', alpha=0.3, label='Quadrant III')
    plt.axhspan(y_min, 0, xmin=(0 - x_min) / (x_max - x_min), xmax=x_max, facecolor='moccasin', alpha=0.3, label='Quadrant IV')

    # Set x and y limits to the actual plot limits
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    # Add title, labels, grid, and legend
    plt.title("Polizeistreifen vs. Straftaten (Normalized Data)")
    plt.xlabel("Polizeistreifen")
    plt.ylabel("Straftaten")
    plt.grid(True)
    plt.legend()
    plt.savefig("GrundlagenInfo/10_AusDatenLernen/Figures/polizei_vs_kriminalitaet_correl.pdf")  # Save the plot to a PDF file
    plt.show()

visualize_normalized_data(a_diff)
# Calculate correlation coefficient manually
mean_x = a["Polizeistreifen"].mean()
mean_y = a["Straftaten"].mean()

numerator = sum((a["Polizeistreifen"] - mean_x) * (a["Straftaten"] - mean_y))

denominator = ((sum((a["Polizeistreifen"] - mean_x)**2) * sum((a["Straftaten"] - mean_y)**2))**0.5)

correlation_coefficient = numerator / denominator
print(f"Correlation Coefficient (calculated manually): {correlation_coefficient:.2f}, numerator: {numerator:.2f}, denominator: {denominator:.2f}")
