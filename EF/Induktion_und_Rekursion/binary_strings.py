def binary_strings(n, w=""):
    if n == 0:
        print(w)
        return
    binary_strings(n - 1, w + "0")
    binary_strings(n - 1, w + "1")
    return
