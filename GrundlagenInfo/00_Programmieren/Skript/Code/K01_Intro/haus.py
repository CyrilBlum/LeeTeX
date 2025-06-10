import math
import turtle as t

# Tempo der Turtle festlegen
t.speed(1)

# Mauern
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

# Turtle verstecken (damit sie nicht das Haus verdeckt)
t.hideturtle()

# Turtle-Zeichnung stehen lassen
t.done()
