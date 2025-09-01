# Erstellen Sie drei Mengen mit Früchten.
set1 = {'Apfel', 'Banane', 'Orange', 'Traube'}
set2 = {'Banane', 'Orange', 'Kiwi', 'Mango'}
set3 = {'Traube', 'Kiwi', 'Melone'}

## Mengenoperationen und ihre Längen

# Schnittmenge: Finden Sie die gemeinsamen Früchte.
gemeinsame_fruechte = set1 & set2
print("Gemeinsame Früchte zwischen set1 und set2:", gemeinsame_fruechte)
print("Anzahl der gemeinsamen Früchte:", len(gemeinsame_fruechte))

# Vereinigungsmenge: Kombinieren Sie alle einzigartigen Früchte.
alle_fruechte = set1 | set2
print("Alle einzigartigen Früchte aus set1 und set2:", alle_fruechte)
print("Anzahl aller einzigartigen Früchte:", len(alle_fruechte))

# Differenzmenge: Finden Sie die Früchte in set1, die nicht in set3 sind.
nur_in_set1 = set1 - set3
print("Früchte in set1, aber nicht in set3:", nur_in_set1)
print("Anzahl der nur in set1 vorhandenen Früchte:", len(nur_in_set1))