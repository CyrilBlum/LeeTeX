import turtle as t

def halbkreis_left(umfang):
    """macht einen Halkreis als 20-Eck, nach links drehend"""
    for i in range(10):
        t.forward(umfang/40)
        t.left(360 / 20)

def halbkreis_right(umfang):
    """macht einen Halkreis als 20-Eck, nach rechts drehend"""
    for i in range(10):
        t.forward(umfang/40)
        t.right(360 / 20)

t.speed(0)


for _ in range(4):
    halbkreis_left(200)
    halbkreis_right(200)

t.color("gold")
for _ in range(2):
    halbkreis_right(400)
    halbkreis_left(400)
        
    

t.done()