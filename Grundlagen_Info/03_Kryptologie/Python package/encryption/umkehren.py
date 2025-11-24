def umkehren(klartext):
    geheimtext = ""  # leerer String
    b = len(klartext) - 1
    while b >= 0:
        geheimtext += klartext[b]
        b -= 1

    print(geheimtext)


# Verwendung:
umkehren("KANTONSSCHULE")
