import turtle as t

def blatt():
    for _ in range(4):
        t.fd(50)
        t.rt(60)


def blume():
    for _ in range(6):
        blatt()
        t.lt(180)

blume()
t.done()