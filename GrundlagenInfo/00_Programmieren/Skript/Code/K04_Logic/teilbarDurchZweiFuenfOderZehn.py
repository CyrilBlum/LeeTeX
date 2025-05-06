
# Funktion zur Ausgabe des Ergebnisses
def pruefe_teilbarkeit(zahl):
    if zahl % 10 == 0 or zahl % 5 == 0 or zahl % 2 == 0:
        print("Ja, die Zahl ist durch 2, 5 oder 10 teilbar.")
    else:
        print("Nein, die Zahl ist durch keine der Zahlen 2, 5 oder 10 teilbar.")

pruefe_teilbarkeit(10)
pruefe_teilbarkeit(7)
pruefe_teilbarkeit(15)
