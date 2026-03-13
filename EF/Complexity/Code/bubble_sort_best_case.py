def bubble_sort_best_case(A):
    n = len(A)
    anzahl_operationen = 0

    # Prüfe, ob die Liste bereits sortiert ist
    ist_sortiert = True
    for i in range(n - 1):
        anzahl_operationen += 1
        if A[i] > A[i + 1]:
            ist_sortiert = False
            break

    if ist_sortiert:
        print(f"{anzahl_operationen} Operationen wurden benötigt.")
        return A

    # Sortiere die Liste wie gewohnt
    for i in range(n):
        for j in range(0, n - i - 1):
            anzahl_operationen += 1
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

    print(f"{anzahl_operationen} Operationen wurden benötigt.")
    return A

bubble_sort_best_case([6, 4, 9, 1])
bubble_sort_best_case([1, 2, 3, 4, 5, 6, 7, 8, 9])