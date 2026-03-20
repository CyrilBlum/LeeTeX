import turtle
import math

t = turtle.Turtle()
t.speed(0)  # Schnellste Zeichen-Geschwindigkeit

# Startposition
t.penup()
t.setpos(0, 400)
t.pendown()


def zacke():
    t.lt(45)
    t.fd(40)
    t.rt(90)
    t.fd(40)
    t.lt(45)


def reihe():
    for _ in range(10):
        zacke()


t.pu()
t.bk(200)
t.pd()

for _ in range(10):
    reihe()

    t.pu()
    t.bk(10 * 40 * math.sqrt(2))
    t.rt(90)
    t.fd(60)
    t.lt(90)
    t.pd()

t.done()
