def berechne_kcal_tot():
    weitere_zutaten = True
    kcal_total = 0
    while weitere_zutaten:
        kcal = int(input("Wie viele Kalorien hatte das Produkt?"))
        gram = int(input("Wie viel wog das Produkt?"))
        kcal_total += kcal * gram / 100
        weitere_zutaten = input("Gibt es weitere Zutaten? (nur True / False antworten)")=="True"
    return kcal_total

kcal = berechne_kcal_tot()
print("Das Gericht hatte total", kcal, "Kalorien")