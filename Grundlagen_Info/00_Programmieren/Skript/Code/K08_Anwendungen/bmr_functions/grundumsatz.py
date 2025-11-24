def grundumsatz(gewicht, groesse, alter, geschlecht):
    """
    Berechnet den Grundumsatz (BMR) nach der Harris-Benedict-Formel.

    Parameter:
    - gewicht: Gewicht in kg
    - groesse: Körpergrösse in cm
    - alter: Alter in Jahren
    - geschlecht: 'mann' oder 'frau'

    Rückgabe:
    - BMR: Grundumsatz in Kilokalorien
    """
    if geschlecht == "mann":
        bmr = 88.362 + (13.397 * gewicht) + (4.799 * groesse) - (5.677 * alter)
    elif geschlecht == "frau":
        bmr = 447.593 + (9.247 * gewicht) + (3.098 * groesse) - (4.330 * alter)

    return bmr


# berechne grundumsatz
bmr = grundumsatz(75, 180, 30, "mann")
print(f"Der Grundumsatz beträgt {bmr:.2f} Kilokalorien")
