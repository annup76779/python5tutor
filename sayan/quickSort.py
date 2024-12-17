def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # search for pivote
    # first element as pivote
    pivote = arr[0]

    # make two array - lesser and greater
    lesser = []
    greater = []

    # fill both the arrays
    for element in arr[1:]:
        if element <= pivote:
            lesser.append(element)
        else:
            greater.append(element)

    return quick_sort(lesser) + [pivote] + quick_sort(greater)


input_arr = [10, 16, 6, 8, 9, 5]

sorted_arr = quick_sort(input_arr)

print(sorted_arr)

