def binaere_suche(liste, ziel):
    # Definiere die Start- und Endpunkte des Suchbereichs
    links = 0
    rechts = len(liste) - 1

    # Solange der Suchbereich gültig ist, also links <= rechts
    while links <= rechts:
        # Berechne das mittlere Element
        mitte = (links + rechts) // 2

        # Wenn das mittlere Element das gesuchte Ziel ist, gib den Index zurück
        if liste[mitte] == ziel:
            print("Mitte gefunden an Position", mitte)
            break

        # Wenn das Ziel grösser ist als das mittlere Element,
        # dann ist das Ziel im rechten Teil der Liste
        elif liste[mitte] < ziel:
            links = mitte + 1

        # Wenn das Ziel kleiner ist als das mittlere Element,
        # dann ist das Ziel im linken Teil der Liste
        else:
            rechts = mitte - 1


# Beispiel-Liste (muss sortiert sein)
meine_liste = [2, 3, 4, 10, 40]
ziel = 10

# Binäre Suche aufrufen
binaere_suche(meine_liste, ziel)