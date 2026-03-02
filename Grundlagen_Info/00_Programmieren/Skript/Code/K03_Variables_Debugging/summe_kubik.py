x = 1
summe = 0
for _ in range(10):
    kubik = x**3
    print(kubik)
    summe += kubik
    x += 1

print("Die Summe der ersten 10 Kubikzahlen ist ", summe)
