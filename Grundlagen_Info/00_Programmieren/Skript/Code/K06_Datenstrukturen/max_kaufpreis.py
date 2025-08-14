def max_kaufpreis(E, b):
    k0 = (100 * b + 15 * E) / 18
    k1 = 150 * b / 37 + 105 * E / 74

    k = min(min(k0, k1), 5 * E)
    return [k, k - E]