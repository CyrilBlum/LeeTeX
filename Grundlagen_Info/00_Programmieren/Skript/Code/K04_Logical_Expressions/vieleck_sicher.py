import turtle as t

anzahl = int(input("Anzahl der Ecken: "))
seite = int(input("Länge der Seiten: "))
if anzahl == 1:
    print("Es gibt kein 1-Eck")
elif anzahl == 2:
    print("Es gibt kein 2-Eck")
elif anzahl > 2:
    for _ in range(anzahl):
        t.forward(seite)
        t.left(360 / anzahl)
    t.done()
