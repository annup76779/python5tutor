# this program is made for checking if it is the time to work or not based on the time(in single digit) entered by 
# the user

# time = float(input("enter the currnet time")) # variable
# WORK_TIME = 6 # this means that you want it to be a constant
# MARGIN = 2

# # if only works when it is provided with True.

# # an if can exist with else 
# # but an cannot 

# if time >= WORK_TIME+MARGIN:
#     print("Comon, get up... you are sooo late.")
# else:
#     print("uer valalkasdjfjkd")
#     sum_=  32+45

#     if time>=WORK_TIME:
#         print("Its time to work.")
#     else:
#         print("you can sleep man.")

#     print("uer valalkasdjfjkd")
#     sum_=  32+45

# if any given number is only divisible by 3 say it super divident, else if the number is divisible by 5 semi divident
# else if the number is divisible by 7 week divident else bad divident 

userIn = int(input("Enter your number: "))

if userIn % 3 == 0:
    print("Super Divident")
elif userIn % 5 == 0:
    print("Semi Divident")
elif userIn % 7 == 0:
    print("Week Divident")
else:
    print("Bad Divident")