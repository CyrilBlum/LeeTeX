import turtle as t

t.speed(10)
t.penup()

# Farben von Italien gemäss Wikipedia
t.fillcolor(0, 140 / 255, 69 / 255)

t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
t.end_fill()

t.forward(100)

t.fillcolor(244 / 255, 245 / 255, 240 / 255)

t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
t.end_fill()

t.forward(100)

t.fillcolor(205 / 255, 33 / 255, 42 / 255)

t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
t.end_fill()


t.done()
