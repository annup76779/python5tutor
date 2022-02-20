# 1 1 2 3 5 8 13 21 ....

l = int(input("Enter the length of the series: "))

print("1 1", end=" ")
l1, l2 = 1, 1
counter = l-2

while counter > 0:
    l1, l2 = l2, l1+l2
    print(l2, end=" ")
    counter = counter - 1