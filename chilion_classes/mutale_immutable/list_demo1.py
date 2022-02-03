# what are the operations we can do on a list --
# 1. we can create a list
# 2. we can add new data to the list at any index - insertion
# 3. we can delete any data in the list at any index - deletion
# 4. we can replace any data from other data at different index
# 5. You can put any other list in list(no issues in that)
# 6. we can can merge(concatinate) any two or more list together.

# now we are taking about deletion of the data

# there are two way to delete the data
# 1. using pop method
# 2. using remove method

# lst = [78, 90, 67, 56, 45 ,76]
# lets see pop method

# how to decide when to use pop method
# we should use pop method only when we know the index whose data we want to delete 
# or
# if we want to delete item from the end of the list

# lst.pop() # it will remove 76 from the last
# print(lst)

# lets talk about remove

# lst = ["78", 90, 67, "56", 45 ,76]
# # when to use remove method
# # we should use remove method of the list when we have any specific data to delete

# lst.remove(10)
# print(lst)

# I will make two functions 
# I will put then in a list and then I will call both the functions using list

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

func_lst = [add, multiply]

for func in func_lst:
    print(func(78, 19939))

# lists can hold any thing inside them 