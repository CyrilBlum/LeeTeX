# Eingabe der natürlichen Zahl x
x = int(input("Geben Sie eine natürliche Zahl ein: "))

# Überprüfung mit einer for-Schleife
a = 1
for _ in range(x + 1):
    if a * a == x:
        print(f"{x} ist eine Quadratzahl. a = {a}")
        break
    elif a * a > x:
        print(f"{x} ist kein Quadrat.")
        break
    a += 1
