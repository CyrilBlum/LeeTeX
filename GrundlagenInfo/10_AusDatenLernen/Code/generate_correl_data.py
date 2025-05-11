import numpy as np
import pandas as pd

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
    
    else:
        raise ValueError(f"Unbekanntes Szenario: {szenario}")
    
generiere_korrelationsdaten("berufserfahrung_vs_einladung", n=20).to_csv("GrundlagenInfo/10_AusDatenLernen/Code/berufserfahrung_vs_einladung.csv", index=False)
generiere_korrelationsdaten("socialmedia_vs_zufriedenheit", n=20).to_csv("GrundlagenInfo/10_AusDatenLernen/Code/socialmedia_vs_zufriedenheit.csv", index=False)
