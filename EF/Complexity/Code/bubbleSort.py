def bubbleSort(A):
    length = len(A)
    for i in reversed(range(length)):
        swapped = False
        for j in range(i):
            if A[j] > A[j + 1]:
                swapped = True
                A[j], A[j + 1] = A[j + 1], A[j]
        if not swapped:
            break
    return A
