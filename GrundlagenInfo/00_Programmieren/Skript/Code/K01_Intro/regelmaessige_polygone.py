import turtle as t

# 5-Eck
for _ in range(5):
    t.fd(50)
    t.right(360 / 5)

# verschieben ohne zu zeichnen
t.up()
t.fd(120)
t.down()

# 6-Eck
for _ in range(6):
    t.fd(50)
    t.right(360 / 6)

# verschieben ohne zu zeichnen
t.up()
t.fd(120)
t.down()

# 8-Eck
for _ in range(8):
    t.fd(50)
    t.right(360 / 8)

t.done()
