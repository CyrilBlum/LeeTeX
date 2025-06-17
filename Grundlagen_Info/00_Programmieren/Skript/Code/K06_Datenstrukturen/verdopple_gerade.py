daten = [5, 7, 8, 6, 3]

i = 0
for _ in range(len(daten)):
    if daten[i] % 2 == 0:
        daten[i] *= 2
        i += 1

print(daten)  # gibt [5, 7, 16, 12, 3] aus
