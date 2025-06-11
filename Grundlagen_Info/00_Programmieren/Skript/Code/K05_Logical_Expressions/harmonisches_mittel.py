def harmonisches_mittel(a, b):
    if (a == 0) or (b == 0):
        print("Das kann man nicht berechnen.")
    else:
        ergebnis = 2 / ((1 / a) + (1 / b))
        print("Das harmonische Mittel ist: "+str(round(ergebnis, 3)))

# Beispielaufrufe
harmonisches_mittel(9, 5)  # Gibt das harmonische Mittel aus
harmonisches_mittel(0, 5)  # Gibt "Das kann man nicht berechnen." aus