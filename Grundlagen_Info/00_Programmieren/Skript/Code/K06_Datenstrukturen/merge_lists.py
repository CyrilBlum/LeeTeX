def verschmelzen(A, B):
    C = []
    i = 0
    while i < len(A):
        C.append(A[i])
        C.append(B[i])
        i += 1
    print(C)


verschmelzen([4, 2], [5, 9])  # Ausgabe: [4, 5, 2, 9]
