# a good number is number which is completely divisible by 3 and 5

num1000 = [x for x in range(1,1001)]
# print(num1000)

# start lookin from here


for num in range(0, 1000):
	if num1000[num] % (3 * 5):
		