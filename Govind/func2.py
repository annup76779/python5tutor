def take_data():
    english = int(input("Enter the marks of english: "))
    math = int(input("Enter the marks of math: "))
    science = int(input("Enter the marks of Science: "))
    sst = int(input("Enter the marks of sst: "))
    computer = int(input("Enter the marks of computer: "))
    total = int(input("Enter the total marks: "))

    percentage = (english + math +science + sst + computer) / (total/100)
    return english, math,science, sst, computer, percentage


# you have to calculate the percentage of the student -> English, Math, Science, Socail Science, computer
def show_result():
    # English, Math, Science, Socail Science, computer
    english, math, science, sst, computer, percentage = take_data()

    print("English: ", english)
    print("Math: ", math)
    print("Science: ", science)
    print("Socail Science", sst)
    print("Computer: ", computer)
    
    print("Total Percentage: ", percentage)

show_result()