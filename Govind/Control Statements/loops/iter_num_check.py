# we have write a while loop which takes an integer user input in each iteration and checks if it is odd number or even number.
# we have to stop the loop when the user input an empty line

is_started = False
userIn = "Anruag"

while userIn != "":
    if is_started:
        userIn = int(userIn)
        print(userIn, "is odd?", bool(userIn % 2))

    userIn = input("Enter the number you want to check: ") # input takes data as string
    is_started = True
else:
    print("Exiting the program...")

print("ended.")