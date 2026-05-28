zahl = int(input("Geben Sie eine Zahl ein: "))
# Lösung mit not:
print(not ((zahl > 0) or (zahl % 2 == 0)))

# Lösung ohne not:
print(zahl <= 0 and zahl % 2 != 0)
