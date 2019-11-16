def quick_sort(array):
    arr_length = len(array)
    if arr_length < 2:
        return array

    mid = arr_length // 2
    pivot = [array[mid]] * array.count(array[mid])
    less = [element for element in array if element < pivot[0]]
    greater = [element for element in array if element > pivot[0]]
    return quick_sort(less) + pivot + quick_sort(greater)
