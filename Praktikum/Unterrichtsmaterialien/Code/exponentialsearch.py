def exponential_search_game(x):
    previous_low = 0
    current_bound = 1
    while True:
        if x == current_bound:
            return f"I found it! Your number is {current_bound}."
        elif x > current_bound:
            previous_low = current_bound
            current_bound *= 2
        elif x < current_bound:
            if (previous_low + 1) >= current_bound:
                 return "The number was not found after the exponential step."
            return binary_search(list(range(previous_low + 1, current_bound)), x)
        
def binary_search(sorted_collection, item):
    left = 0
    right = len(sorted_collection) - 1
    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return f"I found it! Your number is {sorted_collection[midpoint]}"
        elif item < current_item:
            right = midpoint - 1
        else :
            left = midpoint + 1
    return "Not found in the specified range."
