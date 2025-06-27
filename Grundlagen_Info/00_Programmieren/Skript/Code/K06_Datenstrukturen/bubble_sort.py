def bubble_sort(liste):
    i = 0
    for _ in range(len(liste)-1):
        j = 0
        for _ in range(len(liste)-1-i):
            if liste[j] > liste[j+1]:
                temp = liste[j]
                liste[j] = liste[j+1]
                liste[j+1] = temp
            j += 1
        i += 1
    print(liste)

numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
