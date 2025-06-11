import turtle as t

# dies ist eine spezielle syntax, welche es uns erlaubt, einmal "red", einmal "white" und einmal "blue" für c einzusetzen!
for c in ["red", "white", "blue"]:
    # Fenster einrichten
    t.fillcolor(c)

    t.begin_fill()
    # Stift einstellen
    for _ in range(2):
        t.fd(50)
        t.lt(90)
        t.fd(100)
        t.lt(90)
    t.end_fill()

    t.fd(50)

# Fertig
t.done()
