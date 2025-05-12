def bubble_sort(liste):
    n = len(liste)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if liste[j] > liste[j+1]:
                temp = liste[j]
                liste[j] = liste[j+1]
                liste[j+1] = temp
            j += 1
        i += 1
    return liste

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)