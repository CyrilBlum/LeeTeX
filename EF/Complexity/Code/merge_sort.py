def merge(L, R):
    # L und R sind jeweils bereits sortierte Listen.

    # M wird am Ende len(L) + len(R) viele Elemente haben
    # und eine sortierte Liste sein.
    M = []  # M ist zu Beginn eine leere Liste.

    l = 0  # Laufindex innerhalb der Liste L
    r = 0  # Laufindex innerhalb der Liste R

    # solange weder L noch R vollständig durchlaufen wurden
    while (l < len(L)) and (r < len(R)):
        if L[l] <= R[r]:
            M.append(L[l])
            l = l + 1
        else:
            M.append(R[r])
            r = r + 1

    while l < len(L):
        M.append(L[l])
        l = l + 1
    while r < len(R):
        M.append(R[r])
        r = r + 1
    return M


def merge_sort(A):
    # sortiert die Liste A
    if len(A) == 1:  # Rekursionsanfang
        return A  # Listen der Länge 1 sind schon sortiert.

    # teile A in linke Hälfte und rechte Teile
    if len(A) % 2 == 0:  # falls len(A) gerade ist
        middle = len(A) // 2
    else:  # falls len(A) ungerade ist
        middle = (len(A) // 2) + 1
    L = merge_sort(A[:middle])
    R = merge_sort(A[middle:])
    return merge(L, R)
