# basically there are 3 type of letter cases
# 1. Upper case DIVYA
# 2. Lower case divya
# 3. title case Divya
# -> I Love Making Graphics 

# Extra self made
# -> Capatalized case
# -> I love making graphics 

# -> Swapcase

# for doing all this we have total 5 functions in string
# 1. string.upper()
# 2. string.lower()
# 3. string.title()
# 4. string.capitalize()
# 5. string.swap()

userIn = input("Enter some paragraph:\n")

UPPER = userIn.upper()
LOWER = userIn.lower()
TITLE = userIn.title()
CAPITAL = userIn.capitalize()
SWAP = userIn.swapcase()

print(UPPER) # makes everything capital
print(LOWER) # makes everything lower
print(TITLE) # makes everything title case
print(CAPITAL) # makes everything capitalized
print(SWAP) # if anything is lower then it makes that upper and visa versa

# now we will learn how to check if any string is in any specific case.

print("Is UPPER a upper case?", UPPER.isupper())
print("Is LOWER a lower case?", LOWER.islower())
print("Is TITLE a title case?", TITLE.istitle())

