import turtle as t

def star(laenge):
    for _ in range(5):
        t.forward(laenge)
        t.right(144)

t.lt(90)
t.speed(40)

t.color("gold")
laenge = 20
for _ in range(5):
    star(laenge)
    t.pu()
    t.right(90)
    t.forward(laenge)
    t.left(90)
    t.pd()
    laenge += 20

t.done()