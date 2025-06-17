def skalarprodukt(m, p):
    sp = 0
    i = 0
    for _ in range(len(m)):
        sp += m[i] * p[i]
        i += 1
    print(sp)


# Beispiel
m = [0.8, 1.2, 2.3]  # Mengen in kg
p = [2.0, 2.5, 5.0]  # Preise pro kg
skalarprodukt(m, p)  # Ausgabe: 16.1
