anzahl_felder = int(input("Anzahl Felder (muss eine positive gerade Zahl sein): "))
feld_groesse = int(input("Feldgröße (muss >= 1 sein): "))
upper_left = input("Obere linke Ecke (black oder white): ")
if anzahl_felder <= 0 or anzahl_felder % 2 != 0 or feld_groesse < 1:
    print(
        "anzahl_felder muss eine positive gerade Zahl sein und feld_groesse muss >= 1 sein."
    )
else:
    # Bestimme die Startfarbe
    if upper_left == "black":
        startfarbe = 1
    else:
        startfarbe = 0

    # Erzeuge das Schachbrettmuster
    for zeile in range(anzahl_felder):
        # Bestimme die Farbe der ersten Zelle in der Zeile
        zeilenstartfarbe = (startfarbe + zeile) % 2
        for _ in range(feld_groesse):
            zeile_muster = ""
            for spalte in range(anzahl_felder):
                zellenfarbe = (zeilenstartfarbe + spalte) % 2
                zeile_muster += str(zellenfarbe) * feld_groesse
            print(zeile_muster)