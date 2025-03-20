import math
import turtle as t

t.speed(10000)

# Anzahl zu zeichnender "Halbkreise"
anzahl_halbkreise = 8

# wir stellen einen Viertelkreis durch einen Viertel
# eines  Vieleck dar (je mehr Ecken desto genauer)
anzahl_ecken_viertel = 40

# Startwerte der Fibonacci-Folge
f0 = 0
f1 = 1

for _ in range(anzahl_halbkreise):
    # f2 ist die nächste Zahl der Fibonacci-Folge
    f2 = f0 + f1

    # Kreis
    radius = f2 * 10
    umfang = 2 * radius * math.pi

    # Kantenlänge des Vielecks
    kantenlaenge_vieleck = umfang / (4 * anzahl_ecken_viertel)

    for _ in range(anzahl_ecken_viertel):
        t.fd(kantenlaenge_vieleck)

        # nach einem Viertelkreis haben wir uns um 90 Grad gedreht
        t.rt(90 / anzahl_ecken_viertel)

    # Update der Vorgänger
    f0 = f1
    f1 = f2

t.done()
