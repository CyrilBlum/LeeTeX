def bubble_sort(A):
    n = len(A)
    # Gehe durch alle Elemente der Liste
    for i in range(n):
        # Die letzten i Elemente sind bereits an der richtigen Position
        for j in range(0, n - i - 1):
            # Vergleiche das aktuelle Element mit dem nächsten
            if A[j] > A[j + 1]:
                # Vertausche sie, wenn sie in der falschen Reihenfolge sind
                A[j], A[j + 1] = A[j + 1], A[j]
    return A