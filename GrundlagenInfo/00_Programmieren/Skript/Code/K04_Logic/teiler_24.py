# Programm, das alle Zahlen von 1 bis 24 ausgibt, die keine Teiler von 24 sind
x = 1
for _ in range(24):
    if not 24 % x == 0:
        print(x)
    x += 1
