def bubble_sort(liste):
    # Initialisiere den äusseren Schleifenzähler
    i = 0
    # Äussere Schleife: Wiederhole den Sortiervorgang n-mal
    for _ in range(len(liste) - 1):
        # Initialisiere den inneren Schleifenzähler
        j = 0
        # Innere Schleife: Vergleiche benachbarte Elemente
        for _ in range(len(liste) - 1 - i):
            # Wenn das aktuelle Element grösser als das nächste ist, tausche sie
            if liste[j] > liste[j+1]:
                temp = liste[j]  # Temporäre Variable zum Speichern des Werts
                liste[j] = liste[j+1]  # Tausche die Werte
                liste[j+1] = temp  # Setze den gespeicherten Wert an die neue Position
            j += 1  # Erhöhe den inneren Schleifenzähler
        i += 1  # Erhöhe den äusseren Schleifenzähler
        
    # Gib die sortierte Liste aus
    print(liste)

# Beispielverwendung
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)