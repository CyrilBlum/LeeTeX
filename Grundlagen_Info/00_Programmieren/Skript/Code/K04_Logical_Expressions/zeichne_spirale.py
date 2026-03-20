import turtle as t


def zeichne_spirale(seitenlaenge, winkel, increment):
    while seitenlaenge < 200:
        t.forward(seitenlaenge)
        t.right(winkel)
        seitenlaenge += increment


t.speed(0)
zeichne_spirale(10, 45, 5)
t.done()
