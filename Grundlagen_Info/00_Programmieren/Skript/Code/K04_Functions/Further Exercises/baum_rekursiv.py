import turtle as t

t.tracer(False)


def baum(n, base_len, angle=30):
    """
    zeichnet rekursiv einen Baum mit variabler Verästelung (n) und Länge (base_len)
    """
    # initial arrow
    if n == 1:
        t.fd(base_len * n)
        t.lt(angle)
        t.bk(base_len * 1 / 3 * n)
        t.fd(base_len * 1 / 3 * n)
        t.rt(angle * 2)
        t.bk(base_len * 1 / 3 * n)
        t.fd(base_len * 1 / 3 * n)
        t.lt(angle)
    else:
        if n > 1:
            t.fd(base_len * n)
            t.lt(angle)
            baum(n - 1, base_len, angle)
            t.bk(base_len * (n - 1))
            t.rt(angle * 2)
            baum(n - 1, base_len, angle)
            t.bk(base_len * (n - 1))
            t.lt(angle)


t.lt(90)
t.pu()
t.setpos(0, -200)
t.pd()
baum(15, 5, 20)
t.done()
