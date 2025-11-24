geheime_zahl_als_text = "2_10_38"
meine_liste = geheime_zahl_als_text.split("_")
summe = 0
for i in meine_liste:
    summe += int(i)

print(summe)
