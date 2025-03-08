import turtle as t
import math
t.speed(10000)

x=0
y=1

n_circ = 8 # anzahl halbkreise
steps = 40 # schritte pro halbkreis

for _ in range(n_circ):
    z=x+y # z ist die nächste Zahl der Fibonacci-Serie
    radius = z * 10 # Radius ist z * 10
    circumference = radius * 2 * math.pi # circumference ist der Umfang des GANZEN Kreises
    stepsize = circumference/4/steps # wir machen einen Viertel des Umfangs (circumference / 4) in steps Schritten
    print(stepsize)
    for _ in range(steps):
        t.fd(stepsize)
        t.rt(90/steps)
    
    x=y
    y=z

t.done()
