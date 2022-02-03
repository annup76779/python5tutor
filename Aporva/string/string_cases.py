# in strings the string case allowed are- 
# 1. Capitalze -> means 1st character is in upper case and all of the others are in lower case
# 2. Lowercase -> means all the character are in lower case
# 3. Uppercase -> same as capslock
# 4. swapcase -> if something in upercase then it made lowercase and if in lowercase it is made upercase
# 5. title case -> each and every word's first character will get into upercase. 

# s = "I have come up with an application that suits exactly what is needed by a school to publish their."

# print("for capitalize")
# print(s.capitalize())

# print("\nfor lowercase")
# print(s.lower())

# print("\nfor upercase")
# print(s.upper())

# print("\nfor title")
# print(s.title())

# print("\nfor swapcase")
# print(s.swapcase())



#--------------------------------
# verify the case of the string
#--------------------------------

s1  ="jkaskd" # lowercase
s2 = "ASDFSDF" # upercase
s3 = "Sjaksdjfksd" # titlecase

# for islower() method
print("for s1 -> ", s1.islower()) 

print("for s2 -> ", s2.islower())

print("for s3 -> ", s3.islower())

# for isupper() method
print()

print("for s1 -> ", s1.isupper())
print("for s2 -> ", s2.isupper())
print("for s3 ->", s3.isupper())

# for istitle() method
print()

print("for s1 -> ", s1.istitle())
print("for s2 -> ", s2.istitle())
print("for s3 ->", s3.istitle())