import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def generate_correlated_data(r=0.8, n=200):
    mean = [0, 0]
    cov = [[1, r], [r, 1]]  # covariance matrix
    x, y = np.random.multivariate_normal(mean, cov, n).T
    return x, y

# Generate and save each plot as a separate PDF file
correlations = [1, 0.8, 0.4, 0, -0.4, -0.8, -1]
for r in correlations:
    x, y = generate_correlated_data(r=r)
    plt.figure(figsize=(3, 3))
    plt.scatter(x, y, s=3, color=(0, 0, 139/255))  # Set color to dark blue
    plt.axis('off')
    plt.gca().set_position([0, 0, 1, 1])  # Remove margins
    plt.savefig(f"GrundlagenInfo/10_AusDatenLernen/Figures/correlation_{r}.pdf", 
                bbox_inches='tight', pad_inches=0, transparent=True)  # Set transparent background
    plt.close()


def plot_circular_pattern():
    # Circular pattern (correlation ≈ 0)
    theta = np.linspace(0, 2 * np.pi, 100)
    x = np.cos(theta)
    y = np.sin(theta)
    plt.scatter(x, y, s=3)
    plt.title("Correlation ≈ 0")
    plt.axis('equal')
    plt.show()

# Call the function
plot_circular_pattern()

print(np.sort([7,12,3,18,5,10,1,15,8,14,2,17,6,11,4,16,9,13]))