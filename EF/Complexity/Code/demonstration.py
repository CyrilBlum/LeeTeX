import random
import time
from bubble_sort import bubbleSort
from merge_sort import merge_sort

# Erstelle eine Liste von n ganzen Zahlen
n = 5000
random_numbers = [random.randint(0, 1000000) for _ in range(n)]

# Timing Bubble Sort
start_time = time.time()
bubbleSort(random_numbers.copy())
duration_bubble = time.time() - start_time
print(f"Bubble Sort benötigte: {duration_bubble:.4f} Sekunden")

# Timing Merge Sort
start_time = time.time()
merge_sort(random_numbers.copy())
duration_merge = time.time() - start_time
print(f"Merge Sort benötigte: {duration_merge:.4f} Sekunden")

# Vergleich der Laufzeiten
if duration_merge > 0:
    faktor = duration_bubble / duration_merge
    print(f"merge_sort war {faktor:.1f} mal so schnell wie bubble_sort.")
