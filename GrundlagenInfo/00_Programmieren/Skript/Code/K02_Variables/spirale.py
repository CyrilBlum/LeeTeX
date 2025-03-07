import turtle as t

t.speed(100)

laenge = 10
for _ in range(20):
    t.fd(laenge)
    t.rt(90)
    laenge += 10

t.done()
