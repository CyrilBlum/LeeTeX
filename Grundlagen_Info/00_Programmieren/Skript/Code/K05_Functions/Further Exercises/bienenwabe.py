import turtle as t


def sechseck():
    """zeichnet ein Sechseck"""
    for i in range(6):
        t.fd(50)
        t.lt(60)


def bienenwabe(anzahl):
    """zeichnet eine Bienenwabe mit der Funktion Sechseck"""
    for i in range(anzahl):
        sechseck()
        t.fd(50)
        t.rt(60)


bienenwabe(4)
t.done()
