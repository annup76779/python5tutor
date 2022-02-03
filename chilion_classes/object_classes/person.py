from datetime import datetime, date
# "2020-09-12"


class Person:
    count = 0

    def __init__(self, name, dob, address, father = None, mother = None)-> None:
        self.name = name
        
        self.father = None
        self.mother = None
        if isinstance(father, Person) and isinstance(mother, Person):
            self.father =father
            self.mother =mother

        self.dob = datetime.strptime(dob, "%Y-%m-%d").date()
        self.address = address
        current_date = date.today() # 2021-09-22
        self.age = (current_date - self.dob).days/365

    def __str__(self):
        res = f"name: {self.name} age: {self.age} address: {self.address} dob: {self.dob}"
        if self.father is not None and self.mother is not None:
            res += f"father: {self.father} mother: {self.mother}"

        return res

    def get_parents(self):
        if self.father and self.mother:
            father = str(self.father)
            mother = str(self.mother)
            print(father)
            print(mother)
            return self.father, self.mother
        else:
            print("This person looks like an orphan")


print(__name__)

if __name__ == '__main__':
    p1 = Person(name = "Anurag", dob = "2000-12-04", address = "India")
    Person.count += 1
    p2 = Person(name = "Eda", dob = "2001-12-02", address = "Greece")
    Person.count += 1

    chil1 = Person(name = "Ayush", dob = "2020-09-12", address = "India", father = p1, mother = p2)
    Person.count += 1
    chil2 = Person(name = "Eliana", dob = "2017-12-18", address = "India", father = p1, mother = p2)
    Person.count += 1


    print("number of persons", chil2.count)
    print("number of persons", p1.count)

    p1.get_parents()
    p2.get_parents()
    chil1.get_parents()
    chil2.get_parents()