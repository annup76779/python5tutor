with open("input.txt", "r") as f:
    res = 0
    count = 0
    lines = f.readlines()
    for line in lines:
        if line.strip() == "--------------------------":
            count += 1
            break
        _, marks = line.strip().split()
        marks = float(marks)
        res += marks
        count += 1

with open("input.txt", "w") as f:
    total = "\nTotal - "+str(res)
    percent = "\nPercentage - "+ str(res / (count - 1))
    lines = lines[: count] + [total, percent]
    print(lines)
    f.write("".join(lines))