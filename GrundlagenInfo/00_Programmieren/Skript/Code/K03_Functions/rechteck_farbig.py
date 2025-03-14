import turtle as t

def rechteck_farbig(x, y, farbe, breite, laenge):
    # Start-Position setzen
    t.pu()
    t.setpos(x,y)
    t.pd()

    # Farbiges Rechteck zeichnen
    t.color(farbe)
    t.fillcolor(farbe)
    t.begin_fill()
    for _ in range(2):
        t.fd(breite)
        t.rt(90)
        t.fd(laenge)
        t.rt(90)
    t.end_fill()

rechteck_farbig(50, 100, "red", 20, 30)
rechteck_farbig(-20, 30, "green",50, 10)
rechteck_farbig(90, 150, "yellow",100, 70)