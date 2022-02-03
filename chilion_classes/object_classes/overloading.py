# what is overloading?
# when ever you create multiple same named function or method in same same code base with different signatures, this is called "overloading"


# now the question is what does this different signature means?
# differnet number parameters allowed in a function.

# this add funtion will be adding 2 number  at a time
# def add(num1 , num2):
#     return num1 + num2

# def add(num1, num2, num3):
#     return add(num1 , num2) + num3

# def add(num1, num2, num3, num4):
#     return add(num1 , num2) + add(num3 , num4)

# print(add(1,2,3))

# c, C++, Java

def add(num1, num2, num3 = 0, num4 = 0):
    return num1 + num2 + num3 + num4

print(add(1,2,3))
print(add(10, 12))
print(add(1,2,3,4))
print(add())
# 