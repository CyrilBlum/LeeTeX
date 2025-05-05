import turtle as t

def vielecke_sicher(anzahl, seite):
    if anzahl < 1:
        return
    elif anzahl == 1:
        print("Es gibt kein 1-Eck")
    elif anzahl == 2:
        print("Es gibt kein 2-Eck")
    else:
        for _ in range(anzahl):
            t.forward(seite)
            t.left(360 / anzahl)
        t.done()

# Beispielaufruf
vielecke_sicher(5, 100)