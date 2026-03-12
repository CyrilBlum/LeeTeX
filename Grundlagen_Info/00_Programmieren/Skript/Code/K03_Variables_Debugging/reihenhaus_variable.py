import math
import turtle as t

# Tempo der Turtle festlegen
t.speed(10)

laenge= 50 # Länge der Mauern als Variable speichern

for _ in range(5):
    # Mauern
    for _ in range(3):
        t.fd(laenge)
        t.lt(90)
    t.fd(laenge)
    t.lt(180)
    t.fd(laenge)

    # Dach (rechtwinkliges Dreieck)
    t.pencolor("red")  # setze die Stiftfarbe auf rot
    t.rt(45)
    t.fd(laenge / math.sqrt(2))
    t.rt(90)
    t.fd(laenge / math.sqrt(2))

    # Stiftfarbe zurücksetzen (für die Mauern)
    t.pencolor("black")

    # Stift anheben und zur nächsten Position bewegen
    t.penup()
    t.rt(45)
    t.fd(laenge)
    t.lt(90)
    t.pendown()

# Turtle verstecken (damit sie nicht das Haus verdeckt)
t.hideturtle()

# Turtle-Zeichnung stehen lassen
t.done()
