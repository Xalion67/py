# The function calls itself while the size of the array is not equal to one.
# Returns a single item and compares it with the current one in each call.


def max_element(list):
    if len(list) == 0:
        return None
    if len(list) == 1:
        return list[0]
    max = max_element(list[1:])
    return list[0] if list[0] > max else max


list = [56, 345, 563, 23, 56, 43]
print('Maximum element in array ' + str(list) + ' = ' + str(max_element(list)))
