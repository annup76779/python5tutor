# we want to take multiple input from user in a single line.
# i have to take username, useraddress, usermob number in same line.

def takeInput():
    # this will be responsible for taking user input
    userIn = input("Enter user name,address,mobile_number: \n").split(",")
    return userIn

def main():
    # the main function
    user_in = takeInput()
    print(f"{user_in[0]} lives in {user_in[1]} and you can contact him/her on {user_in[2]}")
    joining(user_in)

def joining(user_in):
    # name --> address --> mobile_number
    s = " --> ".join(user_in)
    print(s)
main()