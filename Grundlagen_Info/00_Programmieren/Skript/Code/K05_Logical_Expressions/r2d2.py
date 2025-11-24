def count_symbol(symbol, word):
    count = 0
    for buchstabe in word:
        if buchstabe == symbol:
            count += 1
    return count


def r2d2(move):
    l = count_symbol("l", move)
    r = count_symbol("r", move)
    o = count_symbol("o", move)
    u = count_symbol("u", move)
    if l - r == 0 and o - u == 0:
        return True
    else:
        return False


print(r2d2("lulurorol"))
print(r2d2("lullrol"))
