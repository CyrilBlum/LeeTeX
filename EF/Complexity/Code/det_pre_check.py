def A_modifiziert(M):
    n = len(M)

    #### Pre-Check ####
    if n == 0:
        return 0

    # --- FALL 1: Nullzeile oder Nullspalte prüfen ---
    # Prüfe Zeilen (O(n^2))
    for i in range(n):
        if all(M[i][j] == 0 for j in range(n)):
            return 0.0  # Sofortiger Abbruch, Ergebnis ist 0

    # Prüfe Spalten (O(n^2))
    for j in range(n):
        if all(M[i][j] == 0 for i in range(n)):
            return 0.0  # Sofortiger Abbruch, Ergebnis ist 0

    # --- FALL 2: Diagonalmatrix prüfen (O(n^2)) ---
    # Eine Matrix ist diagonal, wenn alle Elemente ausserhalb der Hauptdiagonale 0 sind.
    is_diagonal = True
    for i in range(n):
        for j in range(n):
            if i != j and M[i][j] != 0:
                is_diagonal = False
                break
        if not is_diagonal:
            break

    if is_diagonal:
        # Best Case: Produkt der Diagonalelemente berechnen (O(n))
        produkt = 1.0
        for i in range(n):
            produkt *= M[i][i]
        return produkt

    # #### FALLBACK: Originaler Algorithmus A (O(n^3)) ####
    return A(M)
