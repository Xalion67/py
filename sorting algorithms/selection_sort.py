# The function finds the smallest element in the array and returns its index
def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


# The function creates an empty array and enters the loop.
#
# In each iteration of the loop, the function finds the index of the smallest
# element in the source array.
#
# Then, pushes it from the source array into the sorted
def selection_sort(array):
    sorted_array = []
    for i in range(len(array)):
        smallest_index = find_smallest(array)
        sorted_array.append(array.pop(smallest_index))
    return sorted_array


# Work example
source_array = [156, 34, 845, 329, 156, 6, 3, 56, 2, 45, 1, 230, 0]
print('Source array >> ' + str(source_array))

sorted_array = selection_sort(source_array)
print('Sorted array >> ' + str(sorted_array))
