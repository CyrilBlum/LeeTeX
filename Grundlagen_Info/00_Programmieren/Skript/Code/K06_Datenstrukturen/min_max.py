def min_max(liste):
    kleinster = liste[0]
    groesster = liste[0]
    for zahl in liste[1:]:
        if zahl < kleinster:
            kleinster = zahl
        elif zahl > groesster:
            groesster = zahl
    return (kleinster, groesster)


# Einfache Aufrufe / Beispiele (Sek II)
kleinster, groesster = min_max([3, 1, 4, 1, 5, 9])
print(f"Kleinster: {kleinster}, Groesster: {groesster}")
