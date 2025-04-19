# Alle natürlichen Zahlen zwischen 0 und 1000 ausgeben,
# die durch 7, aber nicht durch 3 teilbar sind.

for zahl in range(100):
    if zahl % 7 == 0 and zahl % 3 != 0:
        print(zahl)
