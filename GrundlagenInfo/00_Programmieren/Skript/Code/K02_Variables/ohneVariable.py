import turtle as t
import math

for _ in range(4):
    t.forward(50)
    t.left(90)

t.forward(50)
t.left(135)
t.forward(50 * math.sqrt(2))

t.hideturtle()
t.done()