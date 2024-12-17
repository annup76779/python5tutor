# we will make a program where if any give number is divisible by 3, or that number is divisible by 5 or that number is divisible by both, 3 and 5
# using if else elif ladder
# if ladder code.


n = int(input("Enter a number that is integer: "))
if n % 5 == 0 and n % 3 == 0:
    print("Number must be divisible by both")
elif n % 3 == 0:
    print("Number must be divisible by 3")
elif n % 5 == 0:
    print("Number must be divisible by 5")
else:
    print("Invalid number!")


if n % 5 == 0 and n % 3 == 0:
    print("Number must be divisible by 5 and 3")
else:
    if n % 3 == 0:
        print("number is divisible by 3")
    else:
        if n % 5 == 0:
            print("Number must be divisible by 5")
        else:
            print("Invalid number.")
    
