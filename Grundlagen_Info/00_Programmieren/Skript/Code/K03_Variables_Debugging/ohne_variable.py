import turtle as t
import math

# Zeichne ein Quadrat
for _ in range(4):
    t.forward(50)
    t.left(90)

# Zur linken oberen Ecke des Quadrats bewegen
t.forward(50)
t.left(135)

# Diagonale des Quadrats zeichnen
t.forward(50 * math.sqrt(2))

t.hideturtle()
t.done()
