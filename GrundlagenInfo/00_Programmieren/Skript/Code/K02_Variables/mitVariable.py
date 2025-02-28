import turtle as t
import math

# Wir benutzen die Variable L, um der Länge einen Namen zu geben:
laenge = 200

for _ in range(4):
    t.forward(laenge)
    t.left(90)

t.forward(laenge)
t.left(135)
t.forward(laenge * math.sqrt(2))

t.hideturtle()
t.done()