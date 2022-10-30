strings = ["some789", "th3e4r1e23", "r3oos5ting5", "2honk3honk45"]

for index, string_data in enumerate(strings):
    counter = 0
    for i in string_data:
        if i.isdigit():
            counter += 1
    print(f"{index+1}. {string_data}, {counter} numbers")