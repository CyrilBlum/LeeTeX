def c(L):
    n = len(L)  # Grösse der Probleminstanz
    x = 7
    for k in range(n):
        if L[k] == x:
            return True
    return False