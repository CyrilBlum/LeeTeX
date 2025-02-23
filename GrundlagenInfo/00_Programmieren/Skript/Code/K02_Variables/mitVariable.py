import turtle as t
import math

# Wir benutzen die Variable L, um der Länge einen Namen zu geben:
L = 50
for _ in range(4):
    t.forward(L)
    t.left(90)

t.forward(L)
t.left(135)
t.forward(L * math.sqrt(2))

t.hideturtle()
t.done()