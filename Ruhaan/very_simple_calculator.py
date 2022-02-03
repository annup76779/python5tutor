# here we want to make a calculator which keeps on taking numbers from user and add all the entered number and this program 
# ends only if user leaves any line empty.

def calculator():
	sum_ = 0
	print("Please enter each number in new line and also to stop the code leave a 'line empty'")
	while True:
		num = input()
		if num == "":
			break
		num = int(num)
		sum_ += num

	return sum_

print(calculator())