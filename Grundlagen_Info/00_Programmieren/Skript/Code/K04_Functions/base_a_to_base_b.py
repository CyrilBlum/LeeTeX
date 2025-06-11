def base_a_to_base_b(number_a, a, b):
    # der String number_a ist eine Zahlendarstellung in Basis a
    if number_a == "0":
        return "0"

    number_10 = 0
    k = 0
    n = len(number_a)
    while k < len(number_a):
        number_10 += int(number_a[k]) * a ** (n - 1 - k)
        k += 1

    number_b = ""  # leerer String
    while number_10 > 0:
        number_b += str(number_10 % b)
        number_10 //= b

    return number_b[::-1]


# Beispiel
print(base_a_to_base_b("2310213647", 8, 9))
