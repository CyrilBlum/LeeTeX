import turtle as t

def vieleck_kreis(anzahl_ecken, umfang):
    if anzahl_ecken > 35 and umfang >= 100:
        for _ in range(anzahl_ecken):
            t.fd(umfang / anzahl_ecken)
            t.lt(360 / anzahl_ecken)
    else:
        print("Das Vieleck wird nicht gezeichnet, da die Bedingungen nicht erfüllt sind.")

# Beispielaufruf
vieleck_kreis(40, 220)
t.done()