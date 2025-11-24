import turtle as t


def sechseck():
    for _ in range(6):
        t.fd(30)
        t.rt(60)


def blume():
    for _ in range(10):
        t.fd(100)
        t.lt(60)
        sechseck()
        t.rt(60)
        t.bk(100)
        t.lt(360 / 10)


blume()
t.done()
