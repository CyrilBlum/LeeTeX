import turtle as t


def quadrat(laenge):
    if laenge >= 40:
        for _ in range(4):
            t.forward(laenge)
            t.left(90)


quadrat(100)
t.done()
