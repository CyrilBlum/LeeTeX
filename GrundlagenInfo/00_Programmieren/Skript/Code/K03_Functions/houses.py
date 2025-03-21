import turtle as t
import math

def haus(laenge):
    print(laenge)
    anzahl_mauern = 4
    # Mauern
    for _ in range(anzahl_mauern):
        t.fd(laenge)
        t.lt(90)

    # Bewegung zu Dach hin
    t.lt(90)
    t.fd(laenge)

    # Dach
    t.rt(45)
    t.fd(laenge / math.sqrt(2))
    t.rt(90)
    t.fd(laenge / math.sqrt(2))
    t.rt(45)
    t.fd(laenge)
    t.lt(90)

def haeuserreihe(laenge):
    anzahl_haeuser = 5
    for _ in range(anzahl_haeuser):
        haus(laenge)
        laenge+=10

seitenlaenge = 50
haeuserreihe(seitenlaenge)

# Zeichnung stehen lassen
t.done()