def berechne_durchschnitt(liste):
    summe = 0
    for zahl in liste:
        summe += zahl
    durchschnitt = summe / len(liste)
    print("Der Durchschnittswert der Beträge ist:", durchschnitt)


liste = [5, 0, -2, 3, 51, 8, 13, -100, -10, -1]
berechne_durchschnitt(liste)
