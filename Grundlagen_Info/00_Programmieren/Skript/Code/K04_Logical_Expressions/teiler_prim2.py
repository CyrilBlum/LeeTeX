x = int(input("Geben Sie eine natürliche Zahl x > 1 ein: "))

min_teiler = x
max_teiler = 1
teiler = 2

while True:
    if x % teiler == 0:
        if teiler < min_teiler:
            min_teiler = teiler
        if teiler > max_teiler:
            max_teiler = teiler
    teiler += 1
    if teiler >= x:
        break

if min_teiler == x and max_teiler == 1:
    print(f"{x} ist eine Primzahl.")
else:
    print(f"Der kleinste echte Teiler von {x} ist {min_teiler}.")
    print(f"Der grösste echte Teiler von {x} ist {max_teiler}.")
