import math
import turtle as t

# blauer Teil
t.fillcolor((0, 112 / 255, 180 / 255))
t.begin_fill()
# Stift einstellen

t.fd(100)
t.rt(135)
t.fd(math.sqrt(2 * 100**2))
t.rt(135)
t.fd(100)
t.end_fill()

# weisser Teil
for _ in range(3):
    t.bk(100)
    t.lt(90)

# Fertig
t.done()
