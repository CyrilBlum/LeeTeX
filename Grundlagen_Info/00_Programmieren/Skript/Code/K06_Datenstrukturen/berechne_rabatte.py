def berechne_rabatte(liste_preise, liste_rabatte):
    liste_rabattiert = []

    i = 0

    for _ in range(len(liste_rabatte)):
        preis_rabattiert = liste_preise[i] * (1 - liste_rabatte[i] / 100)
        liste_rabattiert.append(preis_rabattiert)
        i += 1

    print(liste_rabattiert)


# berechne Rabatte
liste_preise = [39.95, 65.95, 66.95, 76.95, 9.95, 10.95, 13.95]
liste_rabatte = [30, 40, 30, 35, 20, 15, 35]
berechne_rabatte(liste_preise, liste_rabatte)
