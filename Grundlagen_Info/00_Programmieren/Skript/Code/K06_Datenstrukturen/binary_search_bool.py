def binaere_suche(liste, ziel):
    links = 0
    rechts = len(liste) - 1
    gefunden = False

    while True:
        if links > rechts:
            break  # Ziel nicht gefunden, Schleife beenden

        mitte = (links + rechts) // 2

        if liste[mitte] == ziel:
            gefunden = True
            print("Ziel Gefunden an Position", mitte)
            break
        elif liste[mitte] < ziel:
            links = mitte + 1
        else:
            rechts = mitte - 1

    if not gefunden:
        print("Ziel nicht gefunden.")


# Beispiel-Liste (muss sortiert sein)
meine_liste = [2, 3, 4, 10, 40]
ziel = 10

# Binäre Suche aufrufen
binaere_suche(meine_liste, ziel)
