# there is a concept in string which is called indexing.

# write a program to replace all the "l"s with "o" in the string


s = "Hello world"
print("negative indexing")
print(s[-4])
print("positive indexing")
print(s[1])

# negative indexing is used to get the string from backward
# positive indexing is used to get the string from front

var = ""
i = 0
count = 1000000
while i <= count:
    var += str(i)
    i+=1

print("counting using for loop\n")
count = 0
for i in var:
    count+=1

print("length of string is", count)
print("\ncounting using len function\n")
print("length of string is",len(var))

# slicing