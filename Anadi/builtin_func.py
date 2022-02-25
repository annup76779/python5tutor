# print() -> used to write any output to std output
# print(67, "is my fav number.") 
# what ever you give it to print(irrespective of datatype) it converts that to string and then
# print it to the std output.

#min(*values) -> gives the minimum value among the collection of data of any type
min(1,2,3,4) # 1

#max(*values) -> gives the maximum value among the collection of data of any type
max(1,2,3,4) # 4

# 78 + 67 * (28+78)
# eval(str_expression) -> give it your mathmatical expression in string format and eval() will give you the result

# input(__prompt:optional)
# this is used to take any input from user as string
userIn = float(input("Enter your number: "))
print("User Entered", userIn, type(userIn))
print("Multiplication is", userIn * 10)