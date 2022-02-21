# user will enter a string and a substring
# you have to replace all the substring with space < >

def replace(str_: str, sub_str: str) -> str:
    max_index = len(str_)
    index = 0
    print([x for x in range(max_index)])
    while sub_str in str_:
        if index < max_index:
            if str_[index] == sub_str: # index = 4
                str_ = str_[0 : index] + " " + str_[index+1 : max_index]
            # leave string as it is
        index+=1
    return str_

new_str = replace("2020/05-23", "-")
print(new_str)