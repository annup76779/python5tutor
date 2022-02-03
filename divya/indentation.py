space = 4
alpha = "EDCBA"
index = 4

while index>=0:
	print(" "*index,end="")
	i = index
	while i <=4:
		print(alpha[i], end="")
		i+=1
	print()
	index -= 1
