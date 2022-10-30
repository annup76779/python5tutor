"""
CP1404 Exam Online Assignment Question
Expected output:

0. Rice -> $3,300.00.
0. Rice -> $4,950.00.
...
1. Belle -> $4,000.00.
1. Belle -> $6,000.00.
...
2. Vicky -> $2,800.00.
2. Vicky -> $4,200.00.
...
3. Colin -> $5,000.00.
3. Colin -> $12,500.00.
...
"""
from employee import Employee


def main():
    data = [("Rice", 3300), ("Belle", 4000), ("Vicky", 2800)]
    employees = []
    for item in data:
        employees.append(Employee(item[0], item[1]))

    another = Employee("Colin", 5000, 3)
    employees.append(another)

    for i in range(len(employees)):
        print("{}. {}.".format(i, employees[i]))
        employees[i].increase_pay()
        print("{}. {}.".format(i, employees[i]))
        print("...")


main()
