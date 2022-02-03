# what is mutable and immutable in python

# mutable means thinks which can be changes or whose data can be changed
# but immutable visa versa

# MUTABLE
# 1. list
# 2. dictionary
# 3. set

# Immutable
# 1. Tuple
# 2. MAP
# 3. range
# 4. strings

# 1. list
# 2. Tuple
# 3. MAP
# 4. Dictionary
# 5. set

# what is list
# list is a data structure which can hold more than one data at a time inside it and each data can be accessed and is independent of other datas


lst = (["Anurag", 7], ["divya", 2], 78, 34,23,1,23,32,435,324,4324,234,235)

print(lst[0]) # this is the way to access the list data

# to change any data of the list 
# lst[1] = "Anurag"
# print(lst)

# there are basically 3 way to delete a date from a list
# using pop
# using remove
# del keyword

# using del keyword
# del lst[1]
# print(lst)

# using the remove keyword
# while 23 in lst:
#     lst.remove(23)
# print(lst)


print(lst)
# no index given so it will remove the last data
lst.pop()
print(lst)

# if we give it an index then it will remove the data at that index
lst.pop(0)

print(lst)









