import turtle as t


def dreieck(laenge):
    for i in range(3):
        t.forward(laenge)
        t.left(120)


def dreiecke_ineinander(anzahl, laenge):
    for i in range(anzahl):
        dreieck(laenge)
        t.forward(laenge / 2)
        laenge = laenge / 2
        t.left(60)


t.speed(0)
dreiecke_ineinander(5, 200)
dreieck(200)
t.done()
