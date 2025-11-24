def dreiertausch(klartext):
    geheimtext = ""  # leerer String
    b = 0
    while b < (len(klartext) - 2):
        geheimtext += klartext[b + 2] + klartext[b + 1] + klartext[b]
        b += 3

    if len(klartext) % 3 == 1:
        # Falls ein einzelnes Zeichen übrig bleibt (Länge ist 1 modulo 3)
        geheimtext += klartext[-1]
    elif len(klartext) % 3 == 2:
        # Falls zwei Zeichen übrig bleiben (Länge ist 2 modulo 3)
        geheimtext += klartext[-2] + klartext[-1]

    print(geheimtext)


# Verwendung:
# dreiertausch("KANTONSSCHULE")
