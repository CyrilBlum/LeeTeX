import turtle as t

t.hideturtle()
t.speed(100)

for _ in range(10):
    # zeichne ein Viereck
    for _ in range(4):
        t.fd(100)
        t.rt(360/4)

    # leichte Rechtsdrehung
    t.rt(360/10)

# Turtle-Zeichnung stehen lassen
t.done()