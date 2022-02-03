# for loops are used when you know the exact number of iterations going to be happend
sum_ = 0
# for number in range(1, 101):
#     sum_ = sum_ + number

# print("Sum of first 100 number:", sum_)

def is_prime(number):
    for x in range(2, int(number ** 0.5)):
        if number % x == 0:
            return False
    return True

LIMIT = int(input("Enter any limit of the prime number: "))
counter = 0 # this will be keeping track of the number of prime number we have in our bucket
num_counter = 1 # this will give the current number
while counter < LIMIT:
    if is_prime(num_counter):
        counter = counter + 1
    sum_ += num_counter
    num_counter += 1

print("Sum of number to 27th prime number is", sum_)