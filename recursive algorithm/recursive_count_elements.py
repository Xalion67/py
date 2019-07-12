# The function checks the length of the array.
# If it is not equal to 1, then it adds one and calls the function
# with the array reduced by 1.


def count_element(list):
    if len(list) == 1:
        return 1
    return 1 + count_element(list[1:])


# Work example
# Length of the array = 7
list = [1, 2, 3, 4, 5, 6, 7]
print('Length array ' + str(list) + ' = ' + str(count_element(list)))
