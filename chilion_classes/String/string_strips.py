# what is this strip in string in python?

# It removes extra spaces from left and right of the string.

# Example -> str = "Hello    "
            #str2 = "   Hello anurag  "
            # str2 = "   Hello"

# I have to print even if the number of characters in a string entered by the user in even number else I have to print odd if the character count is odd

userIn = input("Enter some string: ")
# filtered_input = userIn.strip()
# filtered_input = userIn.lstrip()
filtered_input = userIn.rstrip()
# what does strip() do is -> it removes all the extra spaces from both sides

print(userIn, end=":\n")
print(filtered_input, end=":\n\n")

if len(filtered_input) % 2 == 0:
    print("even")

else:
    print("odd")
    