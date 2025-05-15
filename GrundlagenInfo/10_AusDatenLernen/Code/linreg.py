import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf # statsmodels als smf importieren
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import subprocess
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def exercises_jupyter_nb_3b():
    df = pd.read_csv("GrundlagenInfo/10_AusDatenLernen/Data/polizei_vs_kriminalitaet.csv")
    df.head()
    plt.scatter(df["Polizeistreifen"], df["Straftaten"])
    plt.xlabel("Polizeistreifen (police)")
    plt.ylabel("Straftaten (crime)")
    plt.title("Straftaten vs. Polizeistreifen")
    plt.close()
    #plt.show()

    # Regressionsanalyse
    lm = smf.ols(formula="Polizeistreifen ~ Straftaten", data=df).fit()

    m = lm.params["Straftaten"]
    q = lm.params["Intercept"]

    print("Steigung:", m, "Achsenabschnitt:", q)

    # Vorhersage für 8 Polizeistreifen
    df.plot.scatter(x="Polizeistreifen", y="Straftaten")
    x = df["Straftaten"]
    y = m * x + q
    plt.plot(x, y, color="red", label="Regressionslinie")
    plt.close()
    #plt.show()

    # Vorhersage der Straftaten bei 6 Polizeikontrollen
    polizeikontrollen = 6
    vorhergesagte_straftaten = m * polizeikontrollen + q
    print(f"Vorhergesagte Straftaten bei {polizeikontrollen} Polizeikontrollen: {vorhergesagte_straftaten}")


def exercises_jupyter_nb_3b_2():
    df_cars = pd.read_csv("GrundlagenInfo/10_AusDatenLernen/Data/cars-co2.csv")
    df_cars.head()

    # Streudiagramm für jede unabhängige Variable gegenüber CO2-Emissionen zeichnen
    independent_variables = ['Volume', 'Weight']
    for variable in independent_variables:
        plt.scatter(df_cars[variable], df_cars['CO2'])
        plt.xlabel(variable)
        plt.ylabel('CO2')
        plt.title(f'CO2 vs {variable}')
        #plt.show()
        plt.close()

    # Erstellen eines linearen Modells mit statsmodels
    lm_cars = smf.ols(formula="CO2 ~ Weight + Volume", data=df_cars).fit()

    # Ausgabe der Zusammenfassung des Modells
    print(lm_cars.params)

    # Wie viel CO2 wird bei einem Gewicht von 2000 und einem Volumen von 1000 emittiert?
    gewicht = 2000
    volumen = 1000
    vorhergesagtes_co2 = lm_cars.params["Intercept"] + lm_cars.params["Weight"] * gewicht + lm_cars.params["Volume"] * volumen
    print(f"Vorhergesagtes CO2 bei Gewicht {gewicht} und Volumen {volumen}: {vorhergesagtes_co2}")

def exercises_jupyter_notebook():
    # a) Lösung (nicht sofort ausklappen)
    # Datei einlesen
    x1 = df["Schlafdauer"].min()
    x2 = df["Schlafdauer"].max()
    y1 = df[df["Schlafdauer"] == x1]["Notenschnitt"].values[0]
    y2 = df[df["Schlafdauer"] == x2]["Notenschnitt"].values[0]
    m = (y2 - y1) / (x2 - x1)
    q = y1 - m * x1

    m = (y2 - y1) / (x2 - x1)
    q = y1 - m * x1


def plot_schlafdauer_vs_notenschnitt(draw_2p_reg_line=False):
    # Datei einlesen
    df = pd.read_csv(
        "GrundlagenInfo/10_AusDatenLernen/Data/schlafdauer_vs_notenschnitt.csv")
    # Scatter plot zeichnen und Regressionslinie basierend auf m und q einzeichnen
    plt.scatter(df["Schlafdauer"], df["Notenschnitt"], label="Datenpunkte")

    if draw_2p_reg_line:
        x1 = df["Schlafdauer"].min()
        x2 = df["Schlafdauer"].max()
        y1 = df[df["Schlafdauer"] == x1]["Notenschnitt"].values[0]
        y2 = df[df["Schlafdauer"] == x2]["Notenschnitt"].values[0]
        print(f"x1 = {x1:.2f}, x2 = {x2:.2f}")
        print(f"y1 = {y1:.2f}, y2 = {y2:.2f}")

        m = (y2 - y1) / (x2 - x1)
        q = y1 - m * x1

        print(f"y = {m:.2f}x + {q:.2f}")

        # Vorhersage für 8 Stunden Schlaf
        y_pred = m*8+q
        print(f"Vorhersage für 8 Stunden Schlaf: {y_pred:.2f}")

        # Linie zeichnen basierend auf m und q
        x_values = [df["Schlafdauer"].min(), df["Schlafdauer"].max()]
        y_values = [m * x + q for x in x_values]
        plt.plot(x_values, y_values, color="red", label="Regressionslinie")

    # Achsenbeschriftungen und Legende hinzufügen
    plt.xlabel("Schlafdauer (Stunden)")
    plt.ylabel("Notenschnitt")
    plt.legend()
    plt.tight_layout()
    for format in ["pdf"]:
        # Save the plot to a PDF file with no white margins
        plt.savefig(
            f"GrundlagenInfo/10_AusDatenLernen/Figures/schlafdauer_vs_notenschnitt{('_2p_reg' if draw_2p_reg_line else '')}.{format}", bbox_inches='tight')


def plot_3d_plane_with_points():
    # Reset matplotlib style to default
    plt.rcParams.update(plt.rcParamsDefault)

    # Create a figure and a 3D axis
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Define the grid for the plane
    x = np.linspace(2, 9, 10)
    y = np.linspace(3, 8, 10)
    x, y = np.meshgrid(x, y)

    # Generate random points
    num_points = 50
    x_points = np.random.uniform(3, 9, num_points)
    y_points = np.random.uniform(3, 8, num_points)
    z_points = np.clip(0.5 * x_points + 0.4 * y_points +
                       np.random.uniform(-2, 2, num_points)-2, 1, 6)

    # Perform Ordinary Least Squares (OLS) to calculate m, n, and c
    A = np.column_stack((x_points, y_points))
    A = sm.add_constant(A)  # Adds a column of ones for the intercept term
    model = sm.OLS(z_points, A).fit()
    c, m, n = model.params
    z = m * x + n * y + c

    # Plot the surface
    ax.plot_surface(x, y, z, alpha=0.5, cmap='viridis')

    # Calculate the plane's z values for the random x and y points
    z_plane = m * x_points + n * y_points + c

    # Determine colors and markers: points above the plane are red crosses, below are blue circles
    colors = ['red' if z > z_plane[i]
              else 'blue' for i, z in enumerate(z_points)]
    markers = ['x' if z > z_plane[i] else 'o' for i, z in enumerate(z_points)]

    # Plot the random points with appropriate colors and markers
    for i in range(len(z_points)):
        ax.scatter(x_points[i], y_points[i], z_points[i], c=colors[i],
                   marker=markers[i], label="Datenpunkte" if i == 0 else "", s=20)

    # Set axis labels
    ax.set_xlabel('Schlaf (=x)')
    ax.set_ylabel('Lernaufwand (=y)')
    ax.set_zlabel('Note (=z)', rotation=90)

    # Set the z-axis limits to ensure grades go up to 6 only
    ax.set_zlim(1, 6)

    # Add a legend to the plot
    # ax.legend(loc='upper left', fontsize='small')

    # Show the updated plot
    # Save the plot to a PDF file with no white margins
    plt.savefig("GrundlagenInfo/10_AusDatenLernen/Figures/linreg_3d.pdf")

    # Automatically trim whitespace using pdfcrop
    subprocess.run(["pdfcrop", "--margins", "0 0 0 0",
                    "GrundlagenInfo/10_AusDatenLernen/Figures/linreg_3d.pdf",
                    "GrundlagenInfo/10_AusDatenLernen/Figures/linreg_3d.pdf"], check=True)


if __name__ == "__main__":
    # Call the function to plot the 3D plane with points
    # plot_3d_plane_with_points()
    # plot_schlafdauer_vs_notenschnitt(draw_2p_reg_line=False)
    # plot_schlafdauer_vs_notenschnitt(draw_2p_reg_line=True)
    exercises_jupyter_nb_3b_2()