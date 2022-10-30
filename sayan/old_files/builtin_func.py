# num1 = 987283734
# num2 = 987394239

# bigger = max(num1, num2) # used to get the larger number
# print(bigger)

# minner = min(num1, num2)
# print(minner)

# pie = 22/7
# print(round(pie,4))

# s = ";laklsksdjdflasfweoiladvsalfaskfkaskanvnhiajiuweioruwioeersjfklsadjklfjsakjfwaeofis"
# print(len(s))

# how to get random data in python
# how to get random number between a range

# type or isinstance
# type
var = 1
print(isinstance(var, str)) 


import random

# print(random.randint(0, 9))
# print(random.choice(";laklsksdjdflasfweoiladvsalfaskfkaskanvnhiajiuweioruwioeersjfklsadjklfjsakjfwaeofis"))


# builtin classes
# 1. str()
# 2. int()
# 3. float()
# 4. bool()
var = str(var)

print(isinstance(var, str)) 


# we usually use them as type convertor -> means if we have to make any integer a string we simply use str() to make it string
v = 3432432


# taking data from the user
# we use builtin input()

userIn = input("Enter your name: ")
print("You entered", userIn, type(userIn))

# whenever you use input method the you get the data in string format 
# so the userIn in this case has the datatype string.


# can we make any data entered by the user using input method?
# yes, you can 
# simply wrap the input method into the type convertor class in which
# you want your data.

# int_userIn = int(input("Enter your input again: "))
# print("You entered", int_userIn, type(int_userIn))