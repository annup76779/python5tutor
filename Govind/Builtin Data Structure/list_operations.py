lst = list() # empty list

# insertion 
## insertion at end of the list
lst.append(89)
lst.append(78)
lst.append(104)
lst.append(32)
lst.append(12)
print(lst)

## insertion at any speicific index of the list
lst.insert(3, "anurag")
print(lst)
lst.insert(3, "Gobind")
print(lst)

# deletion
## deletion of last elements
popped_data = lst.pop() # leave pop empty to delete the last element
print(lst, popped_data)

## deletion of data at any specific index of the list
popped_data = lst.pop(3)
print(lst, popped_data)
## deletion by the reference of data 
lst.remove("anurag")
print(lst)
# using del keyword of python
# del lst[1]
# print(lst)

# sorting
## refelect change in the same list
# lst.sort()
# print(lst)
# print(lst)
## creates a new list the the changes/arrangement
sorted_list = sorted(lst)
print(lst, sorted_list)

# reversing the list
# # lst.reverse()
# # print(lst)
# new_lst = reversed(lst)
# print(list(new_lst))


# slicing of list
# k = lst[1:3]
# print(k)
# print(lst)


nlst = [45,23,23,23,34,4345,64356,3534,5346,46,6345,345,345,34,534]


# starting point is 0 and ending point is somewhere not at edge
snlst = nlst[:9]
# if ending point is the last element but starting point is somewhere not at edge
# snlst =nlst[4:]
# if ending and starting poit are the two ends
# snlst = nlst[::2]
# if nothing is at the edges
# snlst = nlst[1:13:3]


print(snlst)


### use slicing to reverse list
rev_lst = nlst[::-1]
print(rev_lst)