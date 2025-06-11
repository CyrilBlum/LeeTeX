import turtle as t

def zeichne_siebeneckige_spirale(startlaenge, verkleinerung):
    seitenlaenge = startlaenge
    winkel = 360 / 7  # Winkel für ein Siebeneck

    while seitenlaenge > 10:
        t.forward(seitenlaenge)
        t.right(winkel)
        seitenlaenge -= verkleinerung

# Turtle-Setup
t.speed(0)  # Maximale Geschwindigkeit
t.penup()
t.goto(0, 0)
t.pendown()

# Parameter für die Spirale
startlaenge = 100  # Startlänge der Seite
verkleinerung = 5  # Verkleinerung der Seitenlänge pro Schritt

zeichne_siebeneckige_spirale(startlaenge, verkleinerung)

# Fenster offen halten
t.done()