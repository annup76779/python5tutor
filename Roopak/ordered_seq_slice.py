# slicing works only on in memory ordered sequences

lst = [1,2,34,4,3,345,34,53,463,4,34543,34,634,34,5]

# nlst = lst.copy()
# nlst.reverse()
# print(lst)
# print(nlst)

# if nlst is lst:
#     print(True)

# to eleminate all this 
# slicing can be used as trick
print(lst[::-2])
print(lst[-1])

# 0+(-1) -> -1
