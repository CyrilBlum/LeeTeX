import turtle as t


def zeichne_vieleck(eingabe):
    if eingabe == "1":
        t.color("red")
        for _ in range(4):
            t.forward(100)
            t.right(90)
    elif eingabe == "2":
        t.color("green")
        for _ in range(3):
            t.forward(100)
            t.right(120)
    elif eingabe == "3":
        t.color("blue")
        for _ in range(6):
            t.forward(100)
            t.right(60)
    else:
        print("Nur die Zahlen 1, 2 oder 3 werden als Eingabe akzeptiert.")


# Testaufrufe
zeichne_vieleck("1")  # Test case 1: Red rectangle
zeichne_vieleck("2")  # Test case 2: Green triangle
zeichne_vieleck("3")  # Test case 3: Blue hexagon
zeichne_vieleck("4")  # Test case 4: Invalid input
t.done()
