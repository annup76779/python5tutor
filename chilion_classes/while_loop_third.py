# jhgfjklokjgf


# input from user
userIn = input("I am string hungry! give me string - \n")

# initalizing i = 0
i = 0
# setting increment size
increment = 4

while i < len(userIn): # 

    # i = 0 , it is starting point
    # i + increment = 4 , it is the ending point
    # s = jhgfjklokjgf
    # s[i : i + increment] => 'jhgf'
    sub_str = userIn[i : i + increment]
    if len(sub_str) == 4:
        print(sub_str)
    i  = i + increment
