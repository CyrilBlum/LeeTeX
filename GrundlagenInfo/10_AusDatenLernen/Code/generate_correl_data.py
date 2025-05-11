import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
    elif szenario == "haarlaenge_vs_notenschnitt":
        x = np.random.normal(30, 10, n)  # Haarlänge in cm
        y = np.clip(3 + 0.05 * x + np.random.normal(0, 0.5, n), 1, 6)  # längere Haare → schlechterer Notenschnitt
        
        # Füge Ausreißer hinzu
        num_outliers = max(1, n // 20)  # 1 oder 2 Ausreißer pro 20
        outlier_indices = np.random.choice(n, num_outliers, replace=False)
        y[outlier_indices] = np.random.uniform(1, 6, num_outliers)  # zufällige Werte innerhalb des Notenschnittbereichs
        
        return pd.DataFrame({"Haarlänge (cm)": x, "Notenschnitt": y})
    elif szenario == "schuhgroesse_vs_buecher":
        x = np.random.uniform(0, 100, n)  # Zufällige Werte für X
        y = np.random.uniform(0, 100, n)  # Unabhängige zufällige Werte für Y
        return pd.DataFrame({"Bücher gelesen": x, "Schuhgrösse": y})

    
generiere_korrelationsdaten("berufserfahrung_vs_einladung", n=20).to_csv("GrundlagenInfo/10_AusDatenLernen/Code/berufserfahrung_vs_einladung.csv", index=False)
generiere_korrelationsdaten("socialmedia_vs_zufriedenheit", n=20).to_csv("GrundlagenInfo/10_AusDatenLernen/Code/socialmedia_vs_zufriedenheit.csv", index=False)
generiere_korrelationsdaten("haarlaenge_vs_notenschnitt", n=14, seed=1).to_csv("GrundlagenInfo/10_AusDatenLernen/Code/haarlaenge_vs_notenschnitt.csv", index=False)
