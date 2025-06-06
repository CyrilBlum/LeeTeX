def finde_kleinste_zahl(liste):
    kleinste_zahl = liste[0]
    index_kleinste = 0
    index = 0
    for _ in range(len(liste)):
        if liste[index] < kleinste_zahl:
            kleinste_zahl = liste[index]
            index_kleinste = index
        index += 1
    print(f"Kleinste Zahl: {kleinste_zahl}, Index: {index_kleinste}")

# Beispielaufruf der Funktion
finde_kleinste_zahl([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, -5]) # gibt Kleinste Zahl: -5, Index: 10 aus