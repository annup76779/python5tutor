# which should actually add two numbers and multiply the same two number and print them

def add_number(first_number: int, second_number: int) -> int:
    """
    This will add two number provided while calling the funtion

    Parameter:
        first_number (int) : The fist data to be added
        second_number (int) : The second data to be added

    Return:
        (int) : the addition of the provided data while calling
    """

    return first_number + second_number # 4 + 3

def multiply_number(first_number, second_number):
    return first_number * second_number

def print_them():
    first_data = int(input("Enter the first number "))
    second_data = int(input("Enter the second number "))

    print("The output of addition ", add_number(first_data, second_data))


    print("The output of multiplication", multiply_number(first_data, second_data))

print_them()