def check_palindrom(wort):
    wort = wort.upper()
    if len(wort) <= 1:
        return True
    elif wort[0] != wort[-1]:
        return False
    return check_palindrom(wort[1:-1])