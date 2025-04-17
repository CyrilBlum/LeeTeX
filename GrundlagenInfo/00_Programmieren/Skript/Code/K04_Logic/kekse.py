def kekse(n):
    if n > 500 or n < 1:
         print("Ungültige Anzahl Kekse!")
    else:
        print("Es braucht", n // 12, "Kisten für", n,"Kekse.")
        print(n % 12, "Kekse bleiben übrig.")