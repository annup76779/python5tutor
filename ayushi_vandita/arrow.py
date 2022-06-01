n=7
for i in range(n//2):
    no_star=(n//2) - (i + 1)
    for j in range(no_star+1):
        print(end=" ")
    for j in range(i+1):
        print("*", end="")
    print()

n -= n//2
for i in range(n, 0,-1):
    for j in range(n-i):
        print(end=" ")
    for j in range(i):
        print("*",end="")
    print()