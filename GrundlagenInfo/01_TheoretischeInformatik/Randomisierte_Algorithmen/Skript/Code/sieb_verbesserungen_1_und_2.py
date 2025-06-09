import math


def sieb_verbesserungen_1_und_2(n):
    primzahlen = []
    nicht_gestrichen = (n + 1) * [True]

    i = 2
    # abgerundete Quadratwurzel von n
    wurzel_n = int(math.sqrt(n))
    while i <= wurzel_n:
        if nicht_gestrichen[i]:
            j = i * i
            while j <= n:
                nicht_gestrichen[j] = False
                j += i
        i += 1

    # sammle alle nicht gestrichenen Zahlen
    i = 2
    while i <= n:
        if nicht_gestrichen[i]:
            primzahlen.append(i)
        i += 1
    return primzahlen
