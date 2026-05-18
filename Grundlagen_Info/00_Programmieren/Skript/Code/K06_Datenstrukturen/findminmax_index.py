def finde_min_max_und_index(liste):

    min_wert = max_wert = liste[0]
    min_index = max_index = 0

    for i in range(len(liste)):
        if liste[i] < min_wert:
            min_wert = liste[i]
            min_index = i
        if liste[i] > max_wert:
            max_wert = liste[i]
            max_index = i

    return [min_wert, min_index, max_wert, max_index]


# Beispielaufruf:
result = finde_min_max_und_index([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, -5])
print(f"Kleinste Zahl: {result[0]}, Index: {result[1]}")
print(f"Grösste Zahl: {result[2]}, Index: {result[3]}")
