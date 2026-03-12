import turtle as t

laenge = 20
max_gesamtlaenge = 110
anzahl_zacken = max_gesamtlaenge // laenge

for _ in range(anzahl_zacken):
    t.left(60)
    t.forward(laenge)
    t.right(120)
    t.forward(laenge)
    t.left(60)
t.hideturtle()
t.done()