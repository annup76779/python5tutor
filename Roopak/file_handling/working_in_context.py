
with open("leaning.txt", "r") as my_file:
    # k = my_file.read().replace("mode", "Mode")
    lines_lst = my_file.readlines()
    for line_no, line in enumerate(lines_lst):
        if "learned" in line:
            print(True, line_no)
            k = str(lines_lst[line_no])
            k = k.replace("mode", "Mode")
            lines_lst[line_no] = k
            print(lines_lst[line_no], k)

print(lines_lst)
with open("leaning.txt", "w") as my_file:
    my_file.write("".join(lines_lst))