def quick_sort(array: list, left: int, right: int):
    """ Implementation of the original quicksort algorithm """
    i = left
    j = right
    pivot = array[((left + right) // 2) ]

    # Partition
    while (i <= j):
        while(array[i] < pivot):
            i += 1
        while(array[j] > pivot):
            j -= 1
        if (i <= j):
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    
    # Recursion
    if (left < j):
        quick_sort(array, left, j)
    if (i < right):
        quick_sort(array, i, right)
