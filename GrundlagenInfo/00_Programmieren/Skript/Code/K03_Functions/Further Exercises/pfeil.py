import turtle as t

def p():
    t.fd(100)
    t.rt(30)
    t.bk(20)
    t.fd(20)
    t.lt(60)
    t.bk(20)
    t.fd(20)
    t.rt(30)
    t.bk(100)

def pp():
    t.fd(100)
    t.rt(30)
    p()
    t.lt(60)
    p()
    t.rt(30)
    t.bk(100)


def ppp():
    t.fd(100)
    t.rt(30)
    pp()
    t.lt(60)
    pp()
    t.rt(30)
    t.bk(100)

t.lt(90)
ppp()
t.done()