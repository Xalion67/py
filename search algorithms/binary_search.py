# The function searches the index of an element in an array.
def binary_search(item, array):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if item == array[mid]:
            return mid
        elif item > array[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return None


# Work example
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
element_find = binary_search(7, sorted_array)
element_not_find = binary_search(4, sorted_array)

print('Sorted array >> ' + str(sorted_array))
print('Index number 7 in array = ' + str(element_find))
print('Index number 4 in array = ' + str(element_not_find))
