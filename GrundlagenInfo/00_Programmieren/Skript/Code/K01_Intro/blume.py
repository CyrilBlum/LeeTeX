import turtle as t

# t.hideturtle()
t.shape(name="turtle")
# t.speed(10)

for _ in range(10):
    # zeichne ein Viereck
    for _ in range(4):
        t.fd(100)
        t.rt(360 / 4)
    # leichte Rechtsdrehung
    t.rt(360 / 10)

# Turtle-Zeichnung stehen lassen
t.done()