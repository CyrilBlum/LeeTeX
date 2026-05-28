jahr = int(input("Geben Sie eine Jahreszahl ein: "))
print((jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0))
