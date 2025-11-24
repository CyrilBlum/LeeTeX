# Mengen mit Früchten erstellen
set_1 = {"Apfel", "Banane", "Orange", "Traube"}

# Sets können auch aus Listen erstellt werden
liste_2 = ["Banane", "Orange", "Kiwi", "Mango"]
liste_3 = ["Traube", "Kiwi", "Melone"]
# Listen zu Sets konvertieren
set_2 = set(liste_2)
set_3 = set(liste_3)

# Schnittmenge: Finden Sie die gemeinsamen Früchte
gemeinsame_fruechte = set_1 & set_2
print("Gemeinsame Früchte zwischen set_1 und set_2:", gemeinsame_fruechte)
print("Anzahl der gemeinsamen Früchte:", len(gemeinsame_fruechte))

# Vereinigungsmenge: Kombinieren Sie alle einzigartigen Früchte
alle_fruechte = set_1 | set_2
print("Alle einzigartigen Früchte aus set_1 und set_2:", alle_fruechte)
print("Anzahl aller einzigartigen Früchte:", len(alle_fruechte))

# Differenzmenge: Finden Sie die Früchte in set_1, die nicht in set_3 sind
nur_in_set_1 = set_1 - set_3
print("Früchte in set_1, aber nicht in set_3:", nur_in_set_1)
print("Anzahl der nur in set_1 vorhandenen Früchte:", len(nur_in_set_1))
