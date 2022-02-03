class Student:
    collage_name = "St.Peeters School"
    def __init__(self, name):
        self.name = name
        self.__stud_id = None
        self.__fees = None

    def calculatefees(self):
        pass
    def setname(self, name):
        self.name = name
    def setfees(self, fee):
        self.__fees = fee
    def getfees(self):
        return self.__fees
    def getname(self):
        return self.name
    @staticmethod
    def change_collage_name(name):
        Student.collage_name = name

class Dayscholor(Student):
    def __init__(self,fee, food):
        self.__tution_fee = fee
        self.__foodexpence = food

    def calculatefees(self):
        super().setfees(self.__tution_fee+self.__foodexpence)
    def display(self):
        print(super().getfees())

class Hostelite(Student):
    def __init__(self, hostel_fee, exam_fee):
        self.__hostel_fee = hostel_fee
        self.__exam_fee = exam_fee

    def calculatefees(self):
        super().setfees(self.__hostel_fee+self.__exam_fee)

    def display(self):
        print(super().getfees())

if __name__ == '__main__':
    std1 = Dayscholor(3000, 1600)
    std1.calculatefees()
    std1.display()
    std2 = Hostelite(5000, 1700)
    std2.calculatefees()
    std2.display()
    Student.change_collage_name("Prabhat Academy")
    print(Student.collage_name)
