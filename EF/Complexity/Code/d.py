def d(n):
    result = 0
    i = 1
    while i <= n:
        result += i
        # verdopple i in jedem Schleifendurchlauf
        i *= 2
    return result