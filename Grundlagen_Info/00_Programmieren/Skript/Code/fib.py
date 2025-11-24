def zahlen(n):
    x = 1
    for _ in range(n):
        print("Das Quadrat von " + str(x) + " ist " + str(x**2))
        x = x + 1


zahlen(10)
