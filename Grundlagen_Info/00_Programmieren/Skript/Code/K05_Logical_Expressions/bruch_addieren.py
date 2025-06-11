# Eingabe des Wertes x
x = float(input("Geben Sie einen Wert für x ein (zwischen 0.5 und 1): "))

# Initialisierung der Variablen
summe = .5
nenner = 3
anzahl_brueche = 1

# Brüche addieren, solange die Summe kleiner als x ist
while summe < x:
    summe += 1 / nenner
    nenner += 1
    anzahl_brueche += 1
    if anzahl_brueche > 100:
        print("Die Anzahl der addierten Brüche hat 100 überschritten.")
        break

# Ausgabe des Ergebnisses
print(f"Der Nenner des letzten hinzugefügten Bruchs ist {nenner}.")
print(f"Die Gesamtsumme beträgt {summe:.6f}.")
print(f"Die Anzahl der addierten Brüche beträgt {anzahl_brueche}.")
