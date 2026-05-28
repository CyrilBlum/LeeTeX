n = int(input("Anzahl Kekse: "))
if n > 500:
    print("Ungültige Anzahl Kekse!")
elif n < 1:
    print("Ungültige Anzahl Kekse!")
else:
    print("Es braucht", n // 12, "Kisten für", n, "Kekse.")
    print(n % 12, "Kekse bleiben übrig.")
