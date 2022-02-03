# what is while loop

# while loop is used to do some task again and again untill the condition given to the while loop doesn't become false.

# when talking about condition in while actually it works same as if condition but the only difference is that if condition excutes the code inside if block only once but the while loop keeps on executing that code inside it utill that condition doesn't evaluates False or we forcefully exit of the loop.
# var = 5

# if var > 2:# True
# 	print("its if block -", var)

# while var > 2:
# 	print("Its while block -", var)
# 	var-=1 # shorthand


# we want to write a loop which will exit by itself after some number of iteration.
# lets say i want to exit after 3 iterations

def percentage():
	subjectnumber = int(input("Enter the number of subjects: "))
	start = 1
	summ = 0
	while start <= subjectnumber:
		print("Subject", start,":", end=" ")
		summ += int(input())
		start += 1

	percent = (summ/(100*subjectnumber))* 100
	return percent

output = percentage()
print("percentage of the student is:", output)

