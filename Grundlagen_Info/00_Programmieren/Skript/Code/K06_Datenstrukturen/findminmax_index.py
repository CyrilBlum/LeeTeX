def finde_min_max_und_index(liste):
    min_wert = liste[0]
    max_wert = liste[0]
    min_index = 0
    max_index = 0

    i = 0
    for _ in range(len(liste)):
        if liste[i] < min_wert:
            min_wert = liste[i]
            min_index = i
        if liste[i] > max_wert:
            max_wert = liste[i]
            max_index = i
        x

    print(f"Kleinste Zahl: {min_wert}, Index: {min_index}")
    print(f"Grösste Zahl: {max_wert}, Index: {max_index}")


# Beispielaufruf:
finde_min_max_und_index([3, 1, 4, 1, 5, -9, 2, 6, 5, 3, -5])

