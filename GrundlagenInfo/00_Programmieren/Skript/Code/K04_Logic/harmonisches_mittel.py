def harmonisches_mittel(a, b):
    if a == 0 or b == 0:
        print("Das kann man nicht berechnen.")
        return
    else:
        ergebnis = 2 / ((1 / a) + (1 / b))
        print("Das harmonische Mittel ist: "+str(ergebnis))
        return ergebnis

# Beispielaufrufe
harmonisches_mittel(4, 5)  # Gibt das harmonische Mittel aus
harmonisches_mittel(0, 5)  # Gibt "Das kann man nicht berechnen." aus