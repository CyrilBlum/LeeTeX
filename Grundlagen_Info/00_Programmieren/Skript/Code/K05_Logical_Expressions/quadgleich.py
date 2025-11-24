import math


def quadgleich(a, b, c):
    # Berechnung der Diskriminante
    d = b**2 - 4 * a * c

    # Abhängig vom Wert von d die Lösungen bestimmen
    if d < 0:
        print("Keine reellen Lösungen")
    elif d == 0:
        x = -b / (2 * a)
        print("Eine Lösung: x =", x)
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("Zwei Lösungen: x1 =", x1, ", x2 =", x2)


# Testaufrufe
quadgleich(1, -3, 2)  # Zwei Lösungen: x1 = 2.0, x2 = 1.0
quadgleich(1, 2, 1)  # Eine Lösung: x = -1.0
quadgleich(1, 0, 1)  # Keine reellen Lösungen
