def ist_sortiert(liste):
    i = 1
    while i < len(liste):
        if liste[i] < liste[i-1]:
            return False
        i += 1
    return True