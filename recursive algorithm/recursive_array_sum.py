# The function checks the length of the array.
# If the length is not equal to 1,
# then it pushes the last element from the array and calls itself.


def sum_of_array(array):
    if len(array) == 1:
        return array[0]
    return array.pop() + sum_of_array(array)


# Work example
array = [25, 56, 34, 67, 234, 5]
print('Array = ' + str(array))

sum_elements = sum_of_array(array)
print('Amount elements of array = ' + str(sum_elements))
