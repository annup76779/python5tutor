str = "       My name is anurag pandey      "
print("original -> ", str, end=".\n")


# removing the extra whitespaces from left and right side of the string
str1 = str.strip()
print("str1 ->"+ str1, end=".\n")


# removing extra whitespaces from left side of the string
str2 = str.lstrip()
print("str2 ->"+ str2, end=".\n")

# removing extra whitespaces from right side of the string
str2 = str.rstrip()
print("str2 ->"+ str2, end=".\n")