import turtle as t

anzahl_ecken = int(input("Anzahl der Ecken: "))
umfang = int(input("Umfang des Vielecks: "))
if anzahl_ecken > 35 and umfang >= 100:
    for _ in range(anzahl_ecken):
        t.fd(umfang / anzahl_ecken)
        t.lt(360 / anzahl_ecken)
else:
    print(
        "Das Vieleck wird nicht gezeichnet, da die Bedingungen nicht erfüllt sind."
    )
t.done()
