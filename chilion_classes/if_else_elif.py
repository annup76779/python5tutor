# i want to write a program which will check that the var1 value is greater than 5 or not
# var1 = 6


# if var1 > 5:
#     print("Hey you have given me the correct value")
#     print("Hey you guessed the correct number")
# else:
#     print("This was a bad value")
#     print("Your guess was damn bad")


# i want to check if the number provided by the user is greater than 5 or less than 5 or equal to 5
# var2 = 7

# if var2 > 5:
#     print("This number is greater than 5")
# else:
#     if var2 == 5:
#         print("This number is equal to 5")
#     else:
#         print("this number is less than 5")

# this is the different (Python way)  of writting the above program 
# we are actually going to use elif -> else if in python

# if var2 == 5:
#     print("This number is equal to 5")
# elif var2 < 5:
#     print("this number is less than 5")
# else:
#     print("this number is greater than 5")

"""
here we are trying to implement one liner if else

Rule of one liner if else-
rule 1: if and else should be in same line
rule 2: if cannot exist without else here
rule 3: there should be some statement before if to be executed
rule 4: there should be an statement to be executed after if
and 
rule 5: there should be no statement to be executed between if and else
rule 6: there will always be 2 statement with this if else
"""

var3 = 6
print("This is less than 4") if var3 < 5 else print("this is equal to or greater than 5")
