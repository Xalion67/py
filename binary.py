def binary(decimal_number):
    if decimal_number == 0:
        return '0'

    binary_number = ''

    while decimal_number > 0:
        bit = decimal_number % 2
        binary_number = str(bit) + binary_number
        decimal_number = (decimal_number - bit) // 2

    return binary_number
