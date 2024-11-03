def binary_search(list_sorted, item):
    low = 0
    high = len(list_sorted) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list_sorted[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None