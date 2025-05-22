def zaehle_zehn(liste):
    count = 0
    for zahl in liste:
        if zahl == 10:
            count += 1
    print(count)
    
# Beispiel
liste = [1, 2, 3, 10, 4, 10, 5]
anzahl_zehn = zaehle_zehn(liste)