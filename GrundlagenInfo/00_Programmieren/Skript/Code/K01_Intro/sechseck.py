import turtle as t

def sechseck():
    for _ in range(6):
        t.fd(100)
        t.rt(360/6)

sechseck()
t.rt(10)
sechseck()

t.done()