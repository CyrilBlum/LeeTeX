import turtle as t

# Fenster einrichten
t.bgcolor("red")

t.pu()
t.bk(75)
t.pd()

t.fillcolor("white")
t.begin_fill()
# Stift einstellen
for _ in range(4):
    t.fd(50)
    t.lt(90)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.rt(90)
t.end_fill()

# Fertig
t.done()
