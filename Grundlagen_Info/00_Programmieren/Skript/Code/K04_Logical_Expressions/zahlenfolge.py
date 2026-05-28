x = int(input("Geben Sie eine Zahl x > 1 ein: "))
while x > 1:
    print(x, " -> ")
    if x % 2 == 0:
        x = x // 2
    else:
        x = 3 * x + 1
print(x)  # Ausgabe der letzten Zahl (1)

