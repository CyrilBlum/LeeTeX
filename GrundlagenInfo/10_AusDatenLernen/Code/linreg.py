from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import subprocess
import matplotlib.pyplot as plt

def plot_3d_plane_with_points():
    # Create a figure and a 3D axis
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Define the grid for the plane
    x = np.linspace(0, 10, 10)
    y = np.linspace(0, 10, 10)
    x, y = np.meshgrid(x, y)

    # Define the plane equation z = mx + ny + c
    m, n, c = 0.5, 0.2, 1  # Adjust coefficients to ensure z is distributed between 1 and 6
    z = m * x + n * y + c

    # Plot the surface
    ax.plot_surface(x, y, z, alpha=0.5, cmap='viridis')

    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Generate random points
    num_points = 50
    x_points = np.random.uniform(2, 10, num_points)
    y_points = np.random.uniform(2, 9, num_points)
    z_points = np.random.uniform(0, 6, num_points)

    # Calculate the plane's z values for the random x and y points
    z_plane = m * x_points + n * y_points + c

    # Determine colors: points above the plane are red, below are blue
    colors = ['red' if z > z_plane[i] else 'blue' for i, z in enumerate(z_points)]

    # Plot the random points
    ax.scatter(x_points, y_points, z_points, c=colors, label="Random Points", s=20)

    # Set axis labels
    ax.set_xlabel('Schlaf')
    ax.set_ylabel('Lernaufwand')
    ax.set_zlabel('Note', rotation=90)

    # Set the z-axis limits to ensure grades go up to 6 only
    ax.set_zlim(1, 6)

    # Show the updated plot
    plt.savefig("GrundlagenInfo/10_AusDatenLernen/Figures/linreg_3d.pdf")  # Save the plot to a PDF file with no white margins

    # Automatically trim whitespace using pdfcrop
    subprocess.run(["pdfcrop", "--margins", "0 0 0 0", 
                    "GrundlagenInfo/10_AusDatenLernen/Figures/linreg_3d.pdf", 
                    "GrundlagenInfo/10_AusDatenLernen/Figures/linreg_3d.pdf"], check=True)

if __name__ == "__main__":
    # Call the function to plot the 3D plane with points
    plot_3d_plane_with_points()
