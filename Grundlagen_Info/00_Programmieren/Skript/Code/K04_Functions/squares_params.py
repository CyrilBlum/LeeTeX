import turtle as t


def quadrat(laenge):
    for _ in range(4):
        t.fd(laenge)
        t.rt(90)


quadrat(10)
quadrat(20)
quadrat(30)
# etc.
