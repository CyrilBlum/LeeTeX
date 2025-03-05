import turtle as t
import numpy as np
 
laenge = 5
for _ in range(6):
    t.fd(laenge)
    t.rt(90)
    laenge+=5

t.hideturtle()
t.done()