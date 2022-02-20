n = int(input("Enter the number whose factorial you want to find: "))
fact = 1

while n > 1:
    fact *= n # factorial multiplication
    n-=1 # decrementing n


print("Factorial is:", fact)