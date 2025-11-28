def mvm(A, x):
    num_cols = len(x)
    num_rows = len(A) // num_cols
    b = [0] * num_rows

    for i in range(num_rows):
        for j in range(num_cols):
            b[i] += A[i * num_cols + j] * x[j]

    return b
