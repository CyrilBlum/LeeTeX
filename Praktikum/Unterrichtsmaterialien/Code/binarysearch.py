def binary_search(sorted_collection, item): 
    left = 0 
    right = len(sorted_collection) - 1 

    while left <= right: 
        midpoint = left + (right - left) // 2 
        current_item = sorted_collection[midpoint] 
        if current_item == item: 
            return midpoint 
        elif item < current_item:
            right = midpoint - 1
        else: 
            left = midpoint + 1
    return -1
