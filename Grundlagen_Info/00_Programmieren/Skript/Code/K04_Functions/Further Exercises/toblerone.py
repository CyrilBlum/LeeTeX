import turtle as t
def dreieck():
    t.rt(30)
    t.fd(100)
    t.rt(120)
    t.fd(100)
    t.rt(120)
    t.fd(100)
    t.rt(90)

# change initial position
t.pu()
t.bk(200)
t.pd()
# change initial orientation
t.lt(90)

# set faster speed
t.speed(0)

for _ in range(5):
    dreieck()
    t.rt(90)
    t.fd(100)
    t.lt(90)

t.done()