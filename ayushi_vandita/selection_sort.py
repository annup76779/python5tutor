lst = [23,323,23,45,32432,4,24,234]

# bubble sort
for i in range(0, len(lst)): # no of pass
    print("starting pass ", i+1)
    for j in range(0, len(lst)-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j] # swapped the data
            print(lst[:len(lst)-i], lst[len(lst)-i:])

    print("\nEnding pass", i+1, end="\n"+"*"*20)
    print()
