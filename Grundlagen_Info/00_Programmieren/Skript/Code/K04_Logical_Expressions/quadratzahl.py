def ist_quadrat(x):
    a = 1
    while a * a < x:
        a += 1
    if a * a == x:
        print(f"{x} ist eine Quadratzahl. a = {a}")
    else:
        print(f"{x} ist kein Quadrat.")