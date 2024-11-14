def convert_decimal_to_base_b(decimal, basis):

    if decimal == 0:
        return "0"

    base_b_number = ""
    exp = 0
    highest_exp_found = False
    highest_exp = 0

    while decimal > 0:
        while basis**exp <= decimal:
            exp += 1

        if basis**exp > decimal:
            exp -= 1

        if not highest_exp_found:
            highest_exp = exp
            highest_exp_found = True

        a = 1
        while a * basis**exp <= decimal:
            a += 1

        if a * basis**exp > decimal:
            a -= 1

        base_b_number += str(a)
        decimal -= a * basis**exp

    while len(base_b_number) <= highest_exp:
        base_b_number += "0"

    return base_b_number


def convert_decimal_to_base_b_better(decimal, basis):
    if decimal == 0:
        return "0"

    base_b_number = ""
    while decimal > 0:
        base_b_number += str(decimal % basis)
        decimal //= basis

    return base_b_number[::-1]


print(convert_decimal_to_base_b(823, 5))
print(convert_decimal_to_base_b_better(823, 5))
