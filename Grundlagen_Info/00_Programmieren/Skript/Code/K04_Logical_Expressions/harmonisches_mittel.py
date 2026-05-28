a = int(input("Geben Sie die erste Zahl ein: "))
b = int(input("Geben Sie die zweite Zahl ein: "))
if (a == 0) or (b == 0):
    print("Das kann man nicht berechnen.")
else:
    ergebnis = 2 / ((1 / a) + (1 / b))
    print("Das harmonische Mittel ist: " + str(round(ergebnis, 3)))