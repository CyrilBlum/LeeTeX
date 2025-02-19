# berechnet zwar die Summe 9 + 10,
# gibt aber keinen Output (fehlender print)
9 + 10

# es gilt die Konvention 'Punkt vor Strich':
print(5 + 7 * 3)  # äquivalent zu 5 + (7 * 3) = 26

# Summe
5 + 503  # 508
# Differenz
10 - 24  # -14
# Produkt
8 * 5  # 40
# (übliche) Division
10 / 4  # 2.5
# ganzzahlige Division (zwei forward-slashes)
10 // 4  # 2
# Potenz
2**4  # 16

"""
die Quadratwurzel (English: square root, kurz: sqrt)
ist nicht direkt Teil von Python, sondern muss durch eine Import
hinzugefügt werden
"""
import math

math.sqrt(2)  # 1.4142135623730951
