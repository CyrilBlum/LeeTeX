import numpy as np


def max_kaufpreis(E, b, alpha, beta):

    return np.maximum(
        np.minimum(
            np.minimum(
                (b / 3 + alpha * E) / (alpha + beta),
                (15 * b + 45 * alpha * E + 3 * E) / (45 * alpha + 45 * beta + 1),
            ),
            5 * E,
        ),
        E,
    )
