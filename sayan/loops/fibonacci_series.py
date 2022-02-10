# 1 1 2 3 5 8 12 20 ...
# frist 2 number are 1, 1

# you have to print the fibonacci series to the number of elements given by the user

last, second_last = 1, 1
end = int(input("enter the number of elements you want: "))
# 12

print(last, end=" ")

for _ in range(end-1):
    print(last, end=" ")
    last, second_last = (last + second_last) , last