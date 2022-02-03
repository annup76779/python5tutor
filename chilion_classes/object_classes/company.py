
from person import Person

class MYCompanyEmploy:
    empCount = 0

    def __init__(self, person: Person) -> None:
        self.emp =  person
        self.emp_id = MYCompanyEmploy.empCount + 1

    def __str__(self) -> str:
        return f"Emp_id{self.emp_id}\n\nThe employ detail is: \n{self.emp}"

    def __del__(self):
        MYCompanyEmploy.empCount -= 1
        empList[self.emp_id - 1] = None
        print("Deleted")

empList = []

while True:
    check = input("do you have an emp?")
    if check == "y":
        name = input("Enter the emp name: ") 
        dob = input("Enter the dob (YYYY-MM-DD): ")
        address = input("Enter the address: ")

        emp = MYCompanyEmploy(person = Person(name, dob, address))
        empList.append(emp)
        MYCompanyEmploy.empCount += 1
    else:
        break


for emp in empList:
    print(emp)
    print("Emp count at this employ: ", emp.empCount)