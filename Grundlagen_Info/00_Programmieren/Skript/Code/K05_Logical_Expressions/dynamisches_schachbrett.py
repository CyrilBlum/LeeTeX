def dynamisches_schachbrett(anzahl_felder, feld_groesse, upper_left):
    # 1. Die beiden Grund-Strings für die Felder erstellen
    s = "1" * feld_groesse
    w = "0" * feld_groesse

    # 2. Die zwei verschiedenen Zeilen-Muster vorbereiten
    # Muster 1 beginnt mit s, Muster 2 beginnt mit w
    # Wir wiederholen das Paar (s+w) so oft wie nötig
    wiederholungen = anzahl_felder // 2
    zeile_1 = (s + w) * wiederholungen
    zeile_2 = (w + s) * wiederholungen

    # Falls anzahl_felder ungerade ist, müssen wir noch ein halbes Paar anhängen
    # (gemäss Aufgabenstellung ist die Anzahl Felder aber garantiert gerade)
    if anzahl_felder % 2 != 0:
        zeile_1 += s
        zeile_2 += w

    # 3. Start-Muster festlegen
    if upper_left == "black":
        start = zeile_1
        alternative = zeile_2
    else:
        start = zeile_2
        alternative = zeile_1

    # 4. Das Schachbrett ausgeben
    for i in range(anzahl_felder):
        # Wähle abwechselnd das start- oder alternative Muster
        if i % 2 == 0:
            aktuelle_zeile = start
        else:
            aktuelle_zeile = alternative

        # Drucke die Zeile so oft, wie die feld_groesse es verlangt
        for _ in range(feld_groesse):
            print(aktuelle_zeile)


# Beispielaufruf
dynamisches_schachbrett(4, 1, "black")
