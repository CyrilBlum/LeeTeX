def merge_sort(A):
    # sortiert die Liste A
    if len(A) == 1:  # Rekursionsanfang
        return A  # Listen der Länge 1 sind schon sortiert.

    # teile A in eine linke und rechte Hälfte auf
    if len(A) % 2 == 0:  # falls len(A) gerade ist
        middle = len(A) // 2
    else:  # falls len(A) ungerade ist
        middle = (len(A) // 2) + 1

    L = merge_sort(A[:middle])
    R = merge_sort(A[middle:])
    return merge(L, R)