# The function checks the length of the array.
# If it is not equal to 1, then it adds one and calls the function
# with the array reduced by 1.


def count_element(list):
    if len(list) == 1:
        return 1
    return 1 + count_element(list[1:])
