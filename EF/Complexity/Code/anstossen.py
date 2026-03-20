def anstossen(personen):
    """
    jede Person soll mit jeder anderen genau einmal anstossen
    niemand stösst mit sich selber an
    """
    n = len(personen)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            print(personen[i], "mit", personen[j])