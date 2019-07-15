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
