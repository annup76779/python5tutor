# I want to find out all the number which are even in the given list of numbers(in string format)

ListA = ["23", "87", "89", "14", "45", "58", "92", "100", "11"]

# ListA[5] = int(ListA[5]) # "58" -> 58
# # i am changing the value at index 5 in the list to "89"
# print(ListA)

length = len(ListA) # 8
print("length of the list is", length)

for index in range(length):
	print(ListA[index], index)