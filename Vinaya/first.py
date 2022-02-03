# string are of two types
#1. String
# 2. Byte(binary) stings

# what are white spaces?
# \n , \t, \r, " "

month = {
    "1": "Jan", "2": "Feb", "3": "March", "4": "April", "5": "May", "6": "June", "7": "Aug", "8": "Sep"
}

with open(r"E:\Python's Tutor\python\Shreyash\data.csv", "r") as _file:
    lines = _file.readlines()
    print(lines)

    new_ln = [x.split(",") for x in lines[1: ]]
    error = []
    for i in new_ln:
        old_date = i[0].split("-")
        if len(old_date) == 3:
            old_date[1] = month.get(old_date[1].strip("0"))
            if old_date[1] is None:
                error.append(i)
            print(old_date)
            i[0] = " ".join(old_date)
        else:
            error.append(i)


    for i in new_ln:
        print(i)

    # for line in lines:
    #     print(line.strip())