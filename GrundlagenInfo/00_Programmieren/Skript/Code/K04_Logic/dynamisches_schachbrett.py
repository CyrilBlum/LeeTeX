def dynamisches_schachbrett(anzahl_felder, feld_groesse, upper_left):
    if anzahl_felder <= 0 or anzahl_felder % 2 != 0 or feld_groesse < 1:
        print("anzahl_felder muss eine positive gerade Zahl sein und feld_groesse muss >= 1 sein.")
        return
    
    # Bestimme die Startfarbe
    startfarbe = 1 if upper_left == 'black' else 0

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

# Beispielaufruf
dynamisches_schachbrett(4, 1, "black")