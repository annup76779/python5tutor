# fiboacci series - 0 1 1 2 3 5 8 13 21 34
# user have to enter the length of the series
# the lenght will hold the fist two number in in

length = int(input("enter the length of the series"))

num = 0
next = 1

count = 0
print(num, end=" ")

while count < length:
    print(next, end = " ")
    num, next = next, num + next
    count += 1