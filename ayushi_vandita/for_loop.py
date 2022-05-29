'''
take user input from user to print n numeber of stars in the same line

*****
*   *
*   *
*   *
*****
'''
n = int(input("Enter the number of stars: "))


# print hollow pattern for n-2 time as first and the last row is already been printed
for j in range(n):
    if j == 0 or j == n-1:
        # print the bottom most star pattern *****
        for i in range(n): # 0 1 2 3 4 
            print("*", end="")
    else:
        for i in range(n): # 2, 3, 4
            if i == 0 or i == n-1:
                print("*", end="")
                continue
            print(end=" ")
    print()