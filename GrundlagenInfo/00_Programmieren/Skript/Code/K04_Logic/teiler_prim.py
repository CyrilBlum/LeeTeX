# Eingabe der natürlichen Zahl x
x = int(input("Geben Sie eine natürliche Zahl x > 1 ein:\n"))

# Initialisierung der Variablen
min_teiler = 0  # Startwert für den kleinsten Teiler
max_teiler = 0  # Startwert für den grössten Teiler
i = 2  # Startwert für die Suche nach Teilern

# kleinster Teiler > 1
while i < x:
    if x % i == 0:
        min_teiler = i
        break
    i += 1

# grösster Teiler < x
if min_teiler != 0:
    max_teiler = x // min_teiler

# Ausgabe der Ergebnisse
if min_teiler == 0:
    print(x, "ist eine Primzahl.")
else:
    print("kleinste Teiler:", min_teiler)
    print("grösster Teiler:", max_teiler)

