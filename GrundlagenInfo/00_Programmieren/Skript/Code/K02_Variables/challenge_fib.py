import math
import turtle as t

t.speed(10000)

f0 = 0
f1 = 1

n_circ = 8  # anzahl halbkreise
steps = 40  # schritte pro halbkreis

for _ in range(n_circ):
    f2 = f0 + f1  # f2 ist die nächste Zahl der Fibonacci-Serie

    radius = f2 * 10  # Radius ist

    # umfang ist der Umfang des ganzen Kreises f2 * 10
    umfang = radius * 2 * math.pi

    # wir machen einen Viertel des Umfangs (umfang / 4) in steps vielen Schritten
    stepsize = (umfang / 4) / steps
    for _ in range(steps):
        t.fd(stepsize)
        t.rt(90 / steps)

    # Update der Vorgänger
    f0 = f1
    f1 = f2

t.done()
