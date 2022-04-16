
# end = int(input("enter the ending point: "))
# num = 10
# sum_ = 0

# while num <= end:
#     sum_ += num
#     num += 1

# print("sum is", sum_)

with open("../input.txt", "r") as f:
    while True:
        line = f.readline()
        if line.strip() == "":
            # f.seek(0)
            break
        sum_ = 0
        while line.strip() != "":
            if "#" in line:
                line = f.readline()
                continue
            sum_ += int(line)
            line = f.readline()
        print(sum_)