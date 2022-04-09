# user defined function are kind of function which can be modified and used in different at different place 

# : placed out of any kind of bracket means you are going to make a block of code
def add(num1, num2):
    return num1+num2

def factorial(num):
    fact = num
    for i in range(num-1, 1, -1):
        fact *= i
    return fact

def main():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))

    fn1 = n1 ** 7
    fn2 = n2 ** (1/3)

    # when you give any data to the function call, the data given is called arguments
    res  = add(fn1, fn2)
    print("My final result is", res)
    print("Square of res:", res * res)
    k = factorial(int(res))
    print("Factorial of", int(res), "is", k)

main()