def finde_kleinste_zahl(liste):
    kleinste_zahl = liste[0]
    index = 0
    for i, zahl in enumerate(liste):
        if zahl < kleinste_zahl:
            kleinste_zahl = zahl
            index = i
    print(f"Kleinste Zahl: {kleinste_zahl}, Index: {index}")

# Beispielaufruf der Funktion
finde_kleinste_zahl([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, -5]) # gibt -5 und 10 aus
