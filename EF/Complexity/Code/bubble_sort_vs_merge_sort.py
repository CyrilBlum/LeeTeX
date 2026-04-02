import random
import time
from bubble_sort import bubble_sort
from merge_sort import merge_sort

# Erstelle eine Liste von n ganzen Zahlen
n = 30000
random_numbers = [random.randint(0, 1000000) for _ in range(n)]

# Timing bubble_sort
start_time = time.time()
bubble_sort(random_numbers.copy())
duration_bubble = time.time() - start_time
print(f"bubble_sort benötigte: {duration_bubble:.4f} Sekunden")

# Timing merge_sort
start_time = time.time()
merge_sort(random_numbers.copy())
duration_merge = time.time() - start_time
print(f"merge_sort benötigte: {duration_merge:.4f} Sekunden")

# Vergleich der Laufzeiten
if duration_merge > 0:
    faktor = duration_bubble / duration_merge
    print(f"merge_sort war {faktor:.1f} mal so schnell wie bubble_sort.")