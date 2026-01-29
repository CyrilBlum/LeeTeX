import turtle

# Die aeussere Schleife bestimmt, wie viele Quadrate (3) gezeichnet werden
for _ in range(3):

    # Die innere Schleife zeichnet die 4 Seiten eines Quadrats
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)

    # Nach jedem Quadrat: Stift hoch und zum Startpunkt des naechsten Quadrats
    turtle.penup()
    turtle.forward(70)
    turtle.pendown()

turtle.done()
