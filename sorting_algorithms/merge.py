def merge_sort(array):
    def merge(left, right):
        merged_array = []
        while left and right:
            if left[0] < right[0]:
                merged_array.append(left.pop(0))
            else:
                merged_array.append(right.pop(0))
        if left:
            merged_array.extend(left)
        if right:
            merged_array.extend(right)
        return merged_array

    arr_length = len(array)
    if arr_length < 2:
        return array
    mid = arr_length // 2
    array = merge(merge_sort(array[:mid]), merge_sort(array[mid:]))
    return array
