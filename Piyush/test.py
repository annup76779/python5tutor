d1 = {
    "Ironman": 99,
    "Hulk": 88,
    "Chad": 57
}

condition = input("Enter a condition, you can choose any of the 5 possible cases(>,>=, <, <=) and then threshold with no space:").strip()

symbol = ""
threshold = ""

for el in condition:
    if el in {">", "<", "="}:
        symbol += el
    else:
        threshold += el

threshold = float(threshold)

if symbol == ">":
    print("Students whose grade is [greater than threshold", threshold, "] are:")
elif symbol == "<":
    print("Students whose grade is [less than threshold", threshold, "] are:")
elif symbol == "<=":
    print("Students whose grade is [less than and equal threshold", threshold, "] are:")
elif symbol == ">=":
    print("Students whose grade is [greater than and equal threshold", threshold, "] are:")

elif symbol == "=":
    print("Students whose grade is [equal to threshold", threshold, "] are:")

for key, val in d1.items():
    if symbol == ">":
        if val > threshold:
            print(key, "scored", val, "points.")
    elif symbol == "<":
        if val < threshold:
            print(key, "scored", val, "points.")
    elif symbol == "<=":
        if val <= threshold:
            print(key, "scored", val, "points.")
    elif symbol == ">=":
        if val >= threshold:
            print(key, "scored", val, "points.")

    elif symbol == "=":
        if val == threshold:
            print(key, "scored", val, "points.")
