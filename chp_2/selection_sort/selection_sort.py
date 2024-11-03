def min_elem(array):
    smallest_elem = array[0]
    smallest_elem_ind = 0
    for i in range(1, len(array)):
        if smallest_elem > array[i]:
            smallest_elem = array[i]
            smallest_elem_ind = i
    
    return smallest_elem_ind

def selection_sort(array):
    sort_array = []
    for i in range(len(array)):
        smallest_elem_ind = min_elem(array)
        sort_array.append(array.pop(smallest_elem_ind))

    return sort_array

print(selection_sort([5, 3, 6, 2, 10]))