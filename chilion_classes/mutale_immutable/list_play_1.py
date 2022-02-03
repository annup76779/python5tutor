# you have to take some number from the user and then you have show the user all the number's square and cube


# 4
# 5

# [4 * 4, 4 * 4 * 4]
# [5 * 5, 5 * 5 * 5]

# square = lambda x : x**2
# cude = lambda x : x**3
# cal = lambda x : [int(x), square(int(x)), cude(int(x))]

# def main():
#     num_lst = list(map(cal , input("enter all integer number seperated by space:\n").split()))

#     for i in num_lst:
#         print(i)

# if __name__ == '__main__':
#     main()

square = lambda x: x * x
cube = lambda x: square(x) * x


def main():
    userIn = input("Enter the number seperated with space:\n").split()

    for index in range(len(userIn)):
        data = int(userIn[index])
        sublst = [data, square(data), cube(data)]
        print(sublst)


if __name__ == '__main__':
    main()