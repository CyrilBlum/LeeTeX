# Eingabe der natürlichen Zahl x
x = int(input("Geben Sie eine natürliche Zahl x ein: "))

# Initialisierung der Variablen
min_teiler = 0  # Startwert für den kleinsten Teiler
tmax_teiler = x  # Startwert für den größten Teiler
i = 2  # Startwert für die Suche nach Teilern

# Suche nach dem kleinsten Teiler > 1
while i < x:
    if x % i == 0:
        min_teiler = i
        break
    i += 1

# Suche nach dem größten Teiler < x
if min_teiler != 0:
    tmax_teiler = x // min_teiler

# Ausgabe der Ergebnisse
if min_teiler == 0:
    print(f"{x} ist eine Primzahl.")
else:
    print(f"Der kleinste Teiler von {x} größer als 1 ist: {min_teiler}")
    print(f"Der größte Teiler von {x} kleiner als {x} ist: {tmax_teiler}")