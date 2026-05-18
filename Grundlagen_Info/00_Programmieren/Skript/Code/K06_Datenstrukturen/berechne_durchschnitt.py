def berechne_durchschnitt(liste):
    summe = 0
    for zahl in liste:
        summe += zahl
    durchschnitt = summe / len(liste)
    print("Der Durchschnittswert der Beträge ist:", durchschnitt)


def berechne_durchschnitt_mit_index(liste):
    summe = 0
    for i in range(len(liste)):
        summe += liste[i]
    durchschnitt = summe / len(liste)
    print("Der Durchschnittswert der Beträge ist:", durchschnitt)


def berechne_durchschnitt_mit_while(liste):
    summe = 0
    i = 0
    while i < len(liste):
        summe += liste[i]
        i += 1
    durchschnitt = summe / len(liste)
    print("Der Durchschnittswert der Beträge ist:", durchschnitt)


liste = [5, 0, -2, 3, 51, 8, 13, -100, -10, -1]
berechne_durchschnitt(liste)
berechne_durchschnitt_mit_index(liste)
berechne_durchschnitt_mit_while(liste)
