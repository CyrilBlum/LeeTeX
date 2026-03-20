import turtle as t

# don't show turtle moving
t.tracer(False)


def vieleck(ecken, umfang):
    for _ in range(ecken):
        t.fd(umfang / ecken)
        t.rt(360 / ecken)


def vieleck_muster(umfang):
    while umfang > 50:
        if umfang % 20 == 0:
            vieleck(4, umfang)
        else:
            vieleck(36, umfang)
        t.rt(6)
        umfang -= 10


vieleck_muster(600)

t.done()
