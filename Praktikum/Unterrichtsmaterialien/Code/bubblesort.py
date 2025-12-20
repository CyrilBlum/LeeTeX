def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        vertauscht = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                vertauscht = True
        if not vertauscht:
            break
    return arr