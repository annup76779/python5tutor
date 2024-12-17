# stack can be made of any linar data structure
# # list/array are also a linear data structure
# stack is of type `Last in First out Data structure`


import os
from time import sleep

stack = []
for i in range(10):
    os.system("cls")
    stack.append(i)
    print(stack)
    sleep(1)

for i in range(10):
    os.system("cls")
    stack.pop()
    print(stack)
    sleep(1)


# [[[[[][]]]]]
# [][[]](){}[][({})]
# [][)(]

