import turtle as t


def zeichne_vieleck():
    n = int(input("Gib eine Zahl ein"))
    if n == 1:
        t.color("blue")
        for _ in range(4):
            t.forward(100)
            t.right(90)
    elif 2 <= n <= 6:
        t.color("green")
        for _ in range(6):
            t.forward(100)
            t.right(60)
    elif n >= 7:
        t.color("black")
        for _ in range(n):
            t.forward(100)
            t.right(360 / n)
    else:
        print("Bitte eine Zahl grösser oder gleich 1 eingeben.")
    t.done()


zeichne_vieleck()
