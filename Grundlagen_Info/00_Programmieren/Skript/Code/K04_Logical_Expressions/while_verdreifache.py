zahl = int(input("Geben Sie eine Zahl ein: "))
anzahl = 0
while zahl < 1000000:
    zahl *= 3
    print(zahl)
    anzahl += 1
print("Anzahl Verdreifachungen: ", anzahl)

