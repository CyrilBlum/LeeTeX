import turtle as t
import math

# Wir benutzen die Variable 'laenge', um der Länge einen Namen zu geben:
laenge = 50

for _ in range(4):
    t.forward(laenge)
    t.left(90)

t.forward(laenge)
t.left(135)
t.forward(laenge * math.sqrt(2))

t.hideturtle()
t.done()
