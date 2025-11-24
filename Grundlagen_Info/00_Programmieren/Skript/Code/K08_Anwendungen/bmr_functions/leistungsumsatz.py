def berechne_leistungsumsatz(l_zeit, l_kcal):
    """
    Berechnet den Kalorienverbrauch für jede Aktivität.

    Parameter:
    - l_zeit: Liste der Zeit in Minuten für jede Aktivität
    - l_kcal: Liste des Kalorienverbrauchs pro Minute für jede Aktivität

    Rückgabe:
    - Gesamter Leistungsumsatz (also die Summe des gesamten Kalorienverbrauchs über alle Aktivitäten)
    """
    kalorienverbrauch = 0
    i = 0

    for i in range(len(l_zeit)):
        kalorienverbrauch += l_zeit[i] * l_kcal[i]
        i += 1

    return kalorienverbrauch


# Beispiel
l_zeit = [60, 20]  # Zeit in Minuten
l_kcal = [16.5, 6]  # Kilokalorien pro Minute

kalorienverbrauch = berechne_leistungsumsatz(l_zeit, l_kcal)
print(kalorienverbrauch)  # Erwartetes Ergebnis: 1110
