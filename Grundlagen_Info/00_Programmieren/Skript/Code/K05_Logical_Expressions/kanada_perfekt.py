print("Kanada-perfekte Zahlen kleiner als 600:")
zahl = 2
for _ in range(600-2):
    teilersumme = 0
    for teiler in range(2, zahl):
        if zahl % teiler == 0:
            teilersumme += teiler

    ziffernquadratsumme = 0
    for ziffer in str(zahl):
        ziffernquadratsumme += int(ziffer) ** 2

    if teilersumme == ziffernquadratsumme:
        print(
            f"{zahl}: Summe nichttrivialer Teiler = {teilersumme}, "
            f"Quersumme quadrierter Ziffern = {ziffernquadratsumme}"
        )

    zahl += 1