import turtle as t

for _ in range(10):
    # zeichne ein Quadrat
    for _ in range(4):
        t.fd(100)
        t.rt(360 / 4)
    # Rechtsdrehung um 36 Grad
    t.rt(360 / 10)

# Turtle-Zeichnung nicht schliessen
t.done()
