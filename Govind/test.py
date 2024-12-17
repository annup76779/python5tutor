k = 0
msg = "Hello Admin, good to meet you."

# we have to write a while loop that can handle the printing of the message when admin sets k to non zero
while k == 0:
    print(msg)
    k = int(input("Enter you choice (0/1)"))