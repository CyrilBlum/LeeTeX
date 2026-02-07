import turtle as t

# der folgende Befehl sorgt dafür,
# dass die RGB Werte von 0 bis 255 angegeben werden können
# anstatt von 0 bis 1
t.colormode(255)

# Anfangsfarbe grün
r = 0
g = 255
b = 0

# Es sollen 50 Punkte gezeichnet werden, die immer kleiner werden
# der Durchmesser des ersten Punktes soll 500 sein
durchmesser = 500

for _ in range(50):
    t.pencolor(r, g, b)
    t.dot(durchmesser)
    durchmesser -= 10
    g -= 5

t.done()
