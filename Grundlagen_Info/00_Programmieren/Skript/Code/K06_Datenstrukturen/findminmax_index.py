def finde_min_max_und_index(liste):
    if not liste:
        return None  # Leere Liste

    min_wert = max_wert = liste[0]
    min_index = max_index = 0

    for i, zahl in enumerate(liste):
        if zahl < min_wert:
            min_wert = zahl
            min_index = i
        if zahl > max_wert:
            max_wert = zahl
            max_index = i

    return min_wert, min_index, max_wert, max_index

# Beispielaufruf:
result = finde_min_max_und_index([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, -5])
print(f"Kleinste Zahl: {result[0]}, Index: {result[1]}")
print(f"Grösste Zahl: {result[2]}, Index: {result[3]}")
