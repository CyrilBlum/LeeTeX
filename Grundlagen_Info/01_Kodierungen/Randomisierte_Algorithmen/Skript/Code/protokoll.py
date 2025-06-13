import math

import numpy as np


def sieb_verbesserung_1_und_2(n):
    primzahlen = []
    nicht_gestrichen = (n + 1) * [True]

    i = 2
    # abgerundete Quadratwurzel von n
    wurzel_n = int(math.sqrt(n))
    while i <= wurzel_n:
        if nicht_gestrichen[i]:
            primzahlen.append(i)
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


def Nummer(x):
    dec = 0
    power = len(x) - 1

    for ziffer in x:
        dec += int(ziffer) * 2**power
        power -= 1

    return dec


def Bin(n):
    if n == 0:
        return "0"
    binary_str = ""
    while n > 0:
        binary_str = str(n % 2) + binary_str
        n = n // 2
    return binary_str


def is_equal(x, y):
    nx = len(x)
    ny = len(y)

    if nx != ny:
        return False
    for i in range(nx):
        if x[i] != y[i]:
            return False
    return True


def random_primzahl(n):
    primes = sieb_verbesserung_1_und_2(n)
    p = np.random.choice(primes, 1)[0]
    return p


def R1(x):
    n = len(str(x))
    p = random_primzahl(n**2)
    s = Nummer(x) % p
    return [s, p]


def protokoll(x, y):
    sp = R1(x)
    q = Nummer(y) % sp[1]
    if sp[0] == q:
        return True
    else:
        return False


x = "100110101"
y = "100110101"

print(protokoll(x, y))
print(protokoll(x, y))
