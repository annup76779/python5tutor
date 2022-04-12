f = open("simple_file.txt", "r")

n1 = int(f.readline().strip())
n2 = int(f.readline().strip())
if n1 > n2:
    print("first number is greater")
else:
    print("second number is greater")