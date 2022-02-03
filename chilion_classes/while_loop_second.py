# we will check if there is any number in the string provided by the user and print all the found number.

# taking input from user
userIn = input("I am string hungry! Give me string to eat - \n")

# code to filter out all the numbers from the string
i = 0 # making i = 0

numArray = ['0','1','2','3','4','5','6','7','8','9']

while i < len(userIn): # here I am checking the length of the string is greater than i or not
    # all the following line will be excuted for len(userIn) time

    # suppose string is 's5g'
    if userIn[i] in numArray:
        print(userIn[i], end=" ")
    i += 1