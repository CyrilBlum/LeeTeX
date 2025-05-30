def sieb(n):
    # starte mit einer leeren Liste von
    # Primzahlen (wir haben noch keine gefunden)
    primzahlen = []

    # starte mit einer Liste der Länge n + 1
    # nicht_gestrichen[i] ist genau dann True, wenn
    # die Zahl i (i = 0, 1, ..., n) noch
    # nicht gestrichen wurde
    # zu Beginn ist noch keine Zahl durchgestrichen
    nicht_gestrichen = (n + 1) * [True]

    i = 2
    # prüfe, ob die Zahl i (i = 2, ..., n) schon gestrichen ist
    while ...:
        if nicht_gestrichen[i]:
            ...

            # streiche alle Vielfachen von i
            j = 2 * i
            while ...:
                ...
                ...
        i += 1
    return primzahlen
