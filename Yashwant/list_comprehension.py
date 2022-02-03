if __name__ == '__main__':
    x = 1 # i <= x
    y = 1 # j <= y
    z = 2 # k <= z
    n = 3 # sum of i, j, k
    # three co ordinates i, j, k, n -> sum
    lst = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i + j + k) != n]
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for k in range(z+1):
    #             if (i + j + k) != n:
    #                 lst.append([i, j, k])

    print(lst)

