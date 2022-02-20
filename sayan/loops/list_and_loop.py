# I want to find out all the number which are even in the given list of numbers(in string format)

ListA = ["23", "87", "89", "14", "45", "58", "92", "100", "11"]

# ListA[5] = int(ListA[5]) # "58" -> 58
# # i am changing the value at index 5 in the list to "89"
print(ListA)
print("[", end="")
for x in ListA:
	print(f"<{x},{type(x)}>", end=",")
print(']')

length = len(ListA) # 8
print("\n\nlength of the list is", length, end="\n\n")

for index in range(length):
	ListA[index] = int(ListA[index])
	# print(ListA)

print(ListA)
print("[", end="")
for x in ListA:
	print(f"<{x},{type(x)}>", end=",")
print(']')

