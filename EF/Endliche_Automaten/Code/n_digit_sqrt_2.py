from fractions import Fraction

def sqrt2_truncated(n: int) -> str:
    """
    Compute sqrt(2) truncated to n decimal places
    using interval bisection with exact rational arithmetic.
    """

    a = Fraction(1, 1)
    b = Fraction(2, 1)
    scale = 10 ** n

    while True:
        A = (a.numerator * scale) // a.denominator
        B = (b.numerator * scale) // b.denominator

        if A == B:
            break

        m = (a + b) / 2

        if m * m < 2:
            a = m
        else:
            b = m

    D = A
    integer_part = D // scale
    fractional_part = D % scale

    if n == 0:
        return str(integer_part)

    return f"{integer_part}.{fractional_part:0{n}d}"


# example
for i in range(8):
    print(i, sqrt2_truncated(i))