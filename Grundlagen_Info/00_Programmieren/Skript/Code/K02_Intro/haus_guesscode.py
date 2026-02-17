import math
import turtle as t
import time


# Tempo der Turtle festlegen
# t.speed(10)

# Mauern
while True:
    # Zeichne die Mauern des Hauses
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(180)
    t.fd(100)

    # Dach (rechtwinkliges Dreieck)
    t.pencolor("red")  # setze die Stiftfarbe auf rot
    t.rt(45)
    t.fd(100 / math.sqrt(2))
    t.rt(90)
    t.fd(100 / math.sqrt(2))
    print("Länge der Kathete:", 100 / math.sqrt(2))

    time.sleep(1)  # warte 1 Sekunde

    # Turtle verstecken (damit sie nicht das Haus verdeckt)
    t.hideturtle()

    
    t.reset()

# Turtle-Zeichnung stehen lassen    
t.done()
