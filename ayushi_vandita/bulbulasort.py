''' take a list as user input'''

lst = []
n = int(input("Enter the length of the lsit: "))
for i in range(n): # 0 - n-1
    usrIn = input("enter the data: ")
    try:
        data = eval(usrIn) # plan A
    except NameError:
        data = usrIn # plab B

    lst.append(data) # putting data at the end of the list
print(lst)

# lst.sort(key = lambda x: len(x) if isinstance(x, str) else) # inplace sorting
# slst = sorted(lst) # makes a new list with sorted data
# print(slst)
print(lst)


# bubble sort
'''
[4,2,3,1]
after one pass
[2, 3, 1, 4]
[2, 3, 1]
after 1 pass
[2, 1, 3][4]
[2, 1][3,4]
[1], [2, 3 ,4]
[1,2,3,4]
'''

# after each pass the inner comparision of each element in the list will be reduced by one
# for i in range(len(lst)):
#     print("Indexes in")
#     for j in range(0, n - i):
    