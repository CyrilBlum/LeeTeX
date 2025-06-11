import turtle as t

def farb_vieleck(ecken, farbe):
    t.color(farbe)
    for _ in range(ecken):
        t.fd(50)
        t.rt(360/ecken)

farb_vieleck(3,"red")
farb_vieleck(6,"green")
farb_vieleck(4,"blue")

t.done()