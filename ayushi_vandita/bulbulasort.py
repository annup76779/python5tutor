lst = [23,323,23,45,4,32432,24,234]
min_index = 0

print(lst)
# bubble sort
for i in range(len(lst)):
    for j in range(i, len(lst)): # selected area of the array is from i to length of list -1
        if lst[min_index] > lst[j]:
            min_index= j
    lst[min_index], lst[i] = lst[i], lst[min_index]

    print(lst[0: i+1], lst[i+1: ])
    min_index = i+1



print(lst)

# range(0, len(lst)) 0 - 7-1