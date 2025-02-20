import turtle as t

# Tempo der Turtle festlegen
t.speed(100)

# gleichseitiges Dreieck zeichnen
seite = 5
max_seite = 50
increment = 5
while True:
    if seite > max_seite:
        break
    t.fd(seite)
    t.rt(90)
    seite += increment

# Turtle-Zeichnung stehen lassen
t.done()