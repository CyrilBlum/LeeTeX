maximale_summe = 0
beste_a = 0
beste_b = 0
a = 0


for _ in range(10):
    b = 0
    for _ in range(10):
        potenz = a ** b
        aktuelle_summe = 0
        i = 0
        for _ in range(len(str(potenz))):
            ziffer = str(potenz)[i]
            aktuelle_summe += int(ziffer)
            i += 1
        
        if aktuelle_summe > maximale_summe:
            maximale_summe = aktuelle_summe
            beste_a = a
            beste_b = b
        b += 1
    a += 1

print(f"Optimales a: {beste_a}")
print(f"Optimales b: {beste_b}")
print(f"a^b = {beste_a ** beste_b}")
print(f"Maximale Quersumme: {maximale_summe}")