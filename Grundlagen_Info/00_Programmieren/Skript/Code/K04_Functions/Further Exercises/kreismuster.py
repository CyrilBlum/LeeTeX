import turtle as t

# don't show turtle moving
t.tracer(False)

t.hideturtle()
t.speed(0)

def kreis(umfang):
    for _ in range(36):
        t.fd(umfang / 36)
        t.rt(10)

def kreis_muster(anzahl_kreise, umfang):
    for _ in range(anzahl_kreise):
        kreis(umfang)
        t.rt(360 / anzahl_kreise)

kreis_muster(60, 600)
t.done()
