import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_correlated_data(r=0.8, n=200):
    mean = [0, 0]
    cov = [[1, r], [r, 1]]  # covariance matrix
    x, y = np.random.multivariate_normal(mean, cov, n).T
    return x, y


def plot_circular_pattern():
    # Circular pattern (correlation ≈ 0)
    theta = np.linspace(0, 2 * np.pi, 100)
    x = np.cos(theta)
    y = np.sin(theta)
    plt.scatter(x, y, s=3)
    plt.title("Correlation ≈ 0")
    plt.axis('equal')
    plt.show()


def generiere_korrelationsdaten(szenario: str, n: int = 100, seed: int = 42) -> pd.DataFrame:
    np.random.seed(seed)
    
    if szenario == "polizei_vs_kriminalitaet":
        x = np.random.poisson(5, n)  # Polizeistreifen pro Gebiet
        y = np.clip(np.random.normal(loc=x, scale=1, size=n), 0, None)  # mehr Streifen → mehr Meldungen, keine negativen Straftaten
        return pd.DataFrame({"Polizeistreifen": x, "Straftaten": y})
    
    elif szenario == "berufserfahrung_vs_einladung":
        x = np.random.randint(0, 30, n)  # Berufsjahre
        y = 1 / (1 + np.exp(-0.2 * (x - 10))) + np.random.normal(0, 0.05, n)  # logistisches Wachstum
        return pd.DataFrame({"Berufsjahre": x, "Einladungswahrscheinlichkeit": y})
    
    elif szenario == "risikofahren_vs_unfaelle":
        x = np.random.poisson(10, n)  # riskante Manöver
        y = x * 0.3 + np.random.normal(0, 1, n)
        return pd.DataFrame({"Riskante Manöver": x, "Unfälle": y})
    
    elif szenario == "puls_vs_herzinfarkt":
        x = np.random.normal(70, 10, n)  # Puls
        y = np.clip(0.01 * (x - 60)**2 + np.random.normal(0, 1, n), 0, 100)  # Risiko steigt mit Abweichung von Ideal
        return pd.DataFrame({"Ruhepuls": x, "Herzinfarktrisiko (%)": y})
    
    elif szenario == "socialmedia_vs_zufriedenheit":
        x = np.random.poisson(5, n)  # Beiträge pro Tag
        y = np.clip(8 - 0.5 * x + np.random.normal(0, 1, n), 0, 10)  # mehr Beiträge → weniger Zufriedenheit
        return pd.DataFrame({"Beiträge pro Tag": x, "Zufriedenheit (0–10)": y})
    elif szenario == "haarlaenge_vs_note":
        x = np.random.normal(30, 10, n)  # Haarlänge in cm
        y = np.clip(3 + 0.05 * x + np.random.normal(0, 0.5, n), 1, 6)  # längere Haare → schlechtere Note
        
        # Füge Ausreißer hinzu
        num_outliers = max(1, n // 20)  # 1 oder 2 Ausreißer pro 20
        outlier_indices = np.random.choice(n, num_outliers, replace=False)
        y[outlier_indices] = np.random.uniform(1, 6, num_outliers)  # zufällige Werte innerhalb des Notenbereichs
        
        return pd.DataFrame({"Haarlänge (cm)": x, "Note": y})

    elif szenario == "schlafdauer_vs_note":
        x = np.random.normal(7, 1.5, n)  # Schlafdauer in Stunden
        y = np.clip(6 - 0.5 * (8 - x) + np.random.normal(0, 0.3, n), 1, 6)  # mehr Schlaf → bessere Note
        return pd.DataFrame({"Schlafdauer": x, "Note": y})

    elif szenario == "schuhgroesse_vs_buecher":
        x = np.random.uniform(0, 100, n)  # Zufällige Werte für X
        y = np.random.uniform(0, 100, n)  # Unabhängige zufällige Werte für Y
        return pd.DataFrame({"Bücher gelesen": x, "Schuhgrösse": y})

if __name__ == "__main__":
    # Generate and save each plot as a separate PDF file
    correlations = [1, 0.8, 0.4, 0, -0.4, -0.8, -1]
    for r in correlations:
        x, y = generate_correlated_data(r=r)
        plt.figure(figsize=(3, 3))
        plt.scatter(x, y, s=3, color=(0, 0, 139/255))  # Set color to dark blue
        plt.axis('off')
        plt.gca().set_position([0, 0, 1, 1])  # Remove margins
        plt.savefig(f"Grundlagen_Info/10_Aus_Daten_lernen/Figures/correlation_{r}.pdf", 
                    bbox_inches='tight', pad_inches=0, transparent=True)  # Set transparent background
        plt.close()

    # Generate and save correlation data
    generiere_korrelationsdaten("berufserfahrung_vs_einladung", n=20).to_csv("Grundlagen_Info/10_Aus_Daten_lernen/Data/berufserfahrung_vs_einladung.csv", index=False)
    generiere_korrelationsdaten("socialmedia_vs_zufriedenheit", n=20).to_csv("Grundlagen_Info/10_Aus_Daten_lernen/Data/socialmedia_vs_zufriedenheit.csv", index=False)
    generiere_korrelationsdaten("haarlaenge_vs_note", n=14, seed=1).to_csv("Grundlagen_Info/10_Aus_Daten_lernen/Data/haarlaenge_vs_note.csv", index=False)
    generiere_korrelationsdaten("schlafdauer_vs_note", n=25, seed=1).to_csv("Grundlagen_Info/10_Aus_Daten_lernen/Data/schlafdauer_vs_note.csv", index=False)

