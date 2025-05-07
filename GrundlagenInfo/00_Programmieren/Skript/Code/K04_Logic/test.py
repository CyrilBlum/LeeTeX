import turtle as t
def vieleck_kreis(anzahl_ecken, umfang):
    if umfang<100 or anzahl_ecken<=35:
        print("no go")
    else:
        for _ in range(anzahl_ecken):
            t.forward(umfang/anzahl_ecken)
            t.right(360/anzahl_ecken)
        print("here you go :)")

vieleck_kreis(97, 200)