#define any number of interation on the for loop using range(0 = starting point,4 = ending point-1,1)
# range(15,0,-1)
# 15,14,13,12,11,10,9,8,7,6,5,4,3,2,1
# ending value is dependent on the increment value
# if increment value is negative then the ending value will be calculated as ending value+1
# and if the increment value is positive number then the ending value will be calculated as ending value - 1
n = int(input("enter the number: "))
a = n # -> a= 5
# 4,3,2,1 
for i in range(n-1,0,-1):# a= a*i -> a = 20 -> a= 60 -> a= 120 -> a = 120
	a *= i

# from where I am going to get the data
# how I should find the solution
# then checking all the goods and bads of that solution
# then check for the best applied approach of programming to find the code the solution 
# implement it
# run it 
# debug it