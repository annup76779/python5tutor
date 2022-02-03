some_str = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43"

# here we have some_str which has number seprated with spaces. now what we want is to replace each and every space with +.
# there in my mind comes 3 ways to do this
# 1. way is the longest way but the easiest. In this we will put a if condition to check if we are getting a space in the for loop and put 
#   + at the place of " ".

dummy_str = ""
for char in some_str:
    if char == " ":
        dummy_str+="+"
    else:
        dummy_str+= char
    print(dummy_str) # it will run for the complete length of the str.

# 2. we can use string's builtin mothod replace()
print("\nwe are using replace() method")
print(some_str.replace(" ", "+"))

# 3. this is my way to do the same thing which replace() method does.
print("\nusing join() method and split() method of str")
number_str = some_str.split()
new_str = "+".join(number_str)
print(new_str) # it will run to join the number_str list to make the required output
# we have to take out all the number from string as a string format and then make a new str with 