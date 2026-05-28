def summiere(daten):
    i = 0  # Hilfs-Index, um auf Elemente von daten zuzugreifen
    summe = 0  # Variable, um alle Elemente von "daten" zu summieren

    # Jedes Element von Daten zu Summe hinzufügen
    for _ in range(len(daten)):
        print(i, daten[i], summe)
        summe += daten[i]  # Wert von daten[i] zu Summe hinzufügen
        i += 1  # Hilfs-Index um 1 vergrössern (Werte?)
        print(i, daten[i], summe)

    print(summe)


summiere([4, 2, -6, 17, 5, 12])  # Ausgabe: 34
