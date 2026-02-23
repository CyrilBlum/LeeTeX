"""
Aus Wikipedia:

Für das Schweizerkreuz gilt
Das Verhältnis von Breite und Länge beträgt
bei den Kreuzarmen 6 zu 7 und
bei den ganzen Kreuzbalken 6 zu 20.

Der Abstand zwischen Kreuz und Fahnenrand
beträgt auf jeder Seite eine Balkenbreite.

Das Verhältnis der Länge der Kreuzbalken
zur gesamten Seitenlänge der Fahne
beträgt somit 5 zu 8.
"""

import turtle as t

t.speed(10)
t.teleport(-160, -160)
t.penup()

# Rotes Quadrat
t.fillcolor("red")
t.begin_fill()
for _ in range(4):
    t.forward(320)
    t.left(90)
t.end_fill()

# turtle verschieben
t.forward(130)
t.left(90)
t.forward(60)

# weisses Kreuz
t.fillcolor("white")
t.begin_fill()
for _ in range(4):
    t.forward(70)
    t.left(90)
    t.forward(70)
    t.right(90)
    t.forward(60)
    t.right(90)
t.end_fill()

t.done()
