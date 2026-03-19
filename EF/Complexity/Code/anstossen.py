def jeder_mit_jedem(personen):
    """
    jede Person soll mit jeder anderen Person genau einmal anstossen
    keine Person soll mit sich selbst anstossen
    """
    n = len(personen)
    for i in range(n - 1):
        for j in range(i + 1, n):
            print(personen[i], "mit", personen[j])