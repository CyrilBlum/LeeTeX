def vergroessere_um_fuenf(liste):
    i = 0
    for _ in range(len(liste)):
        liste[i] = liste[i] + 5
        i += 1
    
    print(liste)

daten = [20, -7, 8, 2, 1, 6]
vergroessere_um_fuenf(daten)
