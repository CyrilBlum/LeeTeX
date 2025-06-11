import turtle as t

t.hideturtle()
t.speed(0)

def quadrat(seite):
    for _ in range(4):
        t.fd(seite)
        t.rt(90)

def quadrat_reihe(seite, anzahl):
    for _ in range(anzahl):
        quadrat(seite)
        t.pu()
        t.rt(90)
        t.fd(seite)
        t.lt(90)
        t.pd()

def gitter(seite, anzahl_spalten, anzahl_zeilen):
    for _ in range(anzahl_zeilen):
        quadrat_reihe(seite, anzahl_spalten)
        t.pu()
        t.lt(90)
        t.fd(seite * anzahl_spalten)
        t.rt(90)
        t.fd(seite)
        t.pd()
t.lt(90)
gitter(50, 5, 6)
t.done()
