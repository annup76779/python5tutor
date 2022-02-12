'''
user will give marks of any 5 subjects: subjects name to be takes as userInput
Eg: English, Math, Science, Socail Science, computer

>>> user will give those subjects marks as float value 
Enter the marks of English: 89.67
.
.
.

>>> your task if to calculate the percentage of marks and then show the user as output under which do the
student falls.

A -> 90<=marks>=100
B -> 75<=marks>=89
C -> 60<=marks>=74
D -> 50<=marks>=59
otherwise F as he failed the exam
'''

def take_marks_subject_input():
    # taking subject names
    sub1 = input("enter subject1: ")
    sub2 = input("enter subject2: ")
    sub3 = input("enter subject3: ")
    sub4 = input("enter subject4: ")
    sub5 = input("enter subject5: ")

    # taking subject marks
    mark1 = float(input("Enter the marks of "+sub1+": "))
    mark2 = float(input("Enter the marks of "+sub2+": "))
    mark3 = float(input("Enter the marks of "+sub3+": "))
    mark4 = float(input("Enter the marks of "+sub4+": "))
    mark5 = float(input("Enter the marks of "+sub5+": "))

    return sub1, sub2, sub3, sub4, sub5, mark1, mark2, mark3, mark4, mark5

def get_mark_sheet(sub1, sub2, sub3, sub4, sub5, mark1, mark2, mark3, mark4, mark5):
    '''
        A -> 90<=marks>=100
        B -> 75<=marks>=89
        C -> 60<=marks>=74
        D -> 50<=marks>=59
        otherwise F as he failed the exam

        output
        -

        Subject                 Score
        ------------------------------
        English                 89
        Hindi                   71
        Maths                   59
        Science                 72
        SSt                     91
        -------------------------------
        Total                   289
        Percentage              71%
        -------------------------------

    '''
    MAX = 500
    total = mark1 + mark2 + mark3 + mark4 + mark5
    percentage = (total / MAX)* 100
    print("Subject".ljust(24),"Score")
    print("-" * 35)
    print(sub1.title().ljust(24),mark1)
    print(sub2.title().ljust(24),mark2)
    print(sub3.title().ljust(24),mark3)
    print(sub4.title().ljust(24),mark4)
    print(sub5.title().ljust(24),mark5)
    print("-" * 35)
    print("Total".ljust(24),total)
    print("Percentage".ljust(24),percentage, end="%\n")


def main():
    # sub1, sub2, sub3, sub4, sub5, mark1, mark2, mark3, mark4, mark5 = take_marks_subject_input()

    get_mark_sheet(*take_marks_subject_input())

main()