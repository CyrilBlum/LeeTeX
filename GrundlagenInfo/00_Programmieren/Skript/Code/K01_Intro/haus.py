import turtle as t
import math

# Tempo der Turtle festlegen
t.speed(1)

# Mauern
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(180)
t.forward(100)

# Dach (rechtwinkliges Dreieck)
t.pencolor("red") # setze die Stiftfarbe auf rot
t.right(45)
t.forward(100 / math.sqrt(2))
t.right(90)
t.forward(100 / math.sqrt(2))

# Turtle verstecken (damit sie nicht das Haus verdeckt)
t.hideturtle()

# Turtle Zeichnung stehen lassen
t.done()