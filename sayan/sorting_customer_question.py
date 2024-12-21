# (i) Explain how the insertion sort is carried out

def insertion_sort(arr):

    # since we know that the first element is considered sorted in insertion sorting
    # we skip the first element and start the loop from second element.
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1  # previous element

        # while the key is smaller than the previous element
        # we keep of going backwards by subtracting j by 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            # make the current undercheck element equal to the previous element
            """
            [5, 11, 12, 13, 6]
                [5, 11, 12, 6, 13]
                    [5, 11, 6, 12, 13]
                        [5, 6, 11, 12, 13]      
            """

            j -= 1
        arr[j + 1] = key

    return arr


arr = [12, 11, 13, 5, 6]
insertion_sort(arr)

print(arr)

# Best Case: O(n)
# Worst Case: O(n^2)
# Average Case: O(n^2)
