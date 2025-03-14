import turtle as t

# don't show turtle moving
t.tracer(False)

def vieleck(umfang, ecken):
    for _ in range(ecken):
        t.fd(umfang/ecken)
        t.rt(360/ecken)

def vieleck_muster(umfang, ecken):
    for _ in range(60):
        vieleck(umfang, ecken)
        t.rt(6)
        umfang-=10

vieleck_muster(600, 36)
t.done()