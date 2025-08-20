def entferne_duplikate(A):
    B = []

    for a in A:
        a_not_in_b = True
        for b in B:
            if b == a:
                a_not_in_b = False
                break
        if a_not_in_b:
            B.append(a)
    print(B)


# Aufruf:
# entferne_duplikate([94, 3, 94, 2, 1, 1]) # [94, 3, 2, 1]
