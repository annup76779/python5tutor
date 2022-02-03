# so what is set
# set is also an interable over which we can run our our for loop.
# the main feature of set is it don't have permission to have duplicate data

# set1 = {54, 23, 24, 98, 7,43, 123} # sets
# print(set1)

# set2 = set([1,3,43,234,44,3534,43,5345,436,43,543,53,4])


emset = set()
# wait a min 
for num in range(20):
    emset.add(num)

emset.add(5)
emset.add(10)
emset.add(20)

print(emset)

nset = {5, 11, 17, 23, 29, 35}

#----------------------------------
# removing the common of sets
# getting difference of sets
# --------------------------------

# when we use - operator on sets say set1 and set2
# it will make a new set which do not have the common elements of set1 and set2
# lets say set1 = {1, 2, 3, 4, 5}
# and set2= {2,5,6}
# final_set on minus will be {1, 3, 4}


diff2 = emset.difference(nset) # same as emset - nset
print(diff2)

nset.add(12)
diff = diff2 - nset # same as emset
print(diff)


#----------------------------------
# getting the common of sets
# getting the intersection of sets
# --------------------------------

print("intersection of sets;")
intersect = emset.intersection(nset) # getting the common elements in both the setsh
print(intersect)


#----------------------------------
# getting the union of two or more sets
# --------------------------------

new_set = {"Anurag", "Chilion", "Ben", 3432, 23432,234234}

print("\n Learning union")
union1 = emset.union(nset, new_set) #
print(union1)