# # I want to write a program in which i want to check if the string entered by the user is made of all the number or
# # it is made of only alphabets or it is made of alphabets and number both or it is having only white spaces.

# # In programming when I say space it means I am talking about of the whitespace character

# # what are these whitespace characters?
# # ' ', "\t", '\n'
# #  


# userIn = input("Enter something: ")

# # checking if the userinput is made of all the number
# # isnumeric() -> returns True if string has only numbers else False.
# if userIn.isnumeric():
#     print("All the characters are number in this string.")

# # checking if the userinput is made of all the alphabets
# # isalpha() -> returns True if string has only alphabets else False.
# elif userIn.isalpha():
#     print("All the characters are alphabets in this string.")

# # checking if the userinput is made of alphabets and numbers both.
# # isalnum() -> returns True if string has number and alphabets or it has only number or it has only alphabets
# elif userIn.isalnum():
#     print("This string is alphanumeric string.")

# # checking if the userinput is made of whitespaces
# # isspace() -> returns True if string has only whitspaces else False.
# elif userIn.isspace():
#     print("It is a space string.")

# else:
#     print("Some anonymous string.")


# startswith() -> returns True if string starts with any specified character or string else False.

s = "this is python"
print(s.startswith("is")) 

# endswith() -> returns True if string ends with any specified character or string else False.

k = "Anurag teches Python."
print(k.endswith("Python."))