######
# pass
######

# if 5 == 5:
#     pass


#---------------------
# continue / break
#---------------------
# you have to write a program that will take students marks and their name as input, but there is 
# condition that no mark should be greater than 500 and then find the first rank holder.

# NOTE: no limit of student

def get_rank():
    rank_holder, max_marks = "", 0
    number_validity_check_flag = True 
    while True:
        if number_validity_check_flag == True: # X
            name = input("Enter the name of the student: ").strip()
            if name == "": # if there is no name break the loop
                break

        # name => "anurag"
        # prompt for marks -> enter anurag's marks
        mark = float(input("Enter "+name+" marks: ")) # maybe marks are in decimal

        # checking the upper tolerance of marks
        if mark > 500:
            print(f"<<<---Marks must be less than 500, found {mark}--->>>")
            number_validity_check_flag = False
            continue # stop this iteration and continue to other iteration
        else:
            number_validity_check_flag = True

        # finding maximum mark upto now
        if mark > max_marks:
            max_marks = mark
            rank_holder = name

    return rank_holder
# " ".strip() == "" # false

rank_holder_name = get_rank()
print(rank_holder_name, "is the first rank holder in the class.")


# "Anruag    ".strip() -> "Anurag"