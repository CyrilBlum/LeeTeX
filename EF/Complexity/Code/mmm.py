def mmm(A, B, num_rows, num_cols):
    C = [0] * (num_rows * num_cols)

    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(num_cols):
                C[i * num_cols + j] += A[i * num_cols + k] * B[k * num_cols + j]

    return C
