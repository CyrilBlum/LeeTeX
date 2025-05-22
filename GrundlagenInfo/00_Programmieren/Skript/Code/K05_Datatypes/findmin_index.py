def finde_kleinste_zahl(liste):
    kleinste_zahl = liste[0]  # Setze die erste Zahl als kleinste Zahl
    for zahl in liste:
        if zahl < kleinste_zahl:
            kleinste_zahl = zahl  # Aktualisiere die kleinste Zahl
    print(kleinste_zahl)
    
# Beispielaufruf der Funktion
finde_kleinste_zahl([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, -5]) # gibt -5 aus