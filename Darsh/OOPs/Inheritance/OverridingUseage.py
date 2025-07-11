class Marks:
    def __init__(self, value):
        self.value = value

    def rounded(self):
        return round(self.value)

class Subject:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


class BaseResult:
    def __init__(self, title: str, subject: list[Subject]):
        self.title = title
        self.subject = subject

    def print_result(self):
        print(f"Title: {self.title}".center(30))

        print("Subjects:".ljust(12), "Marks".rjust(12), sep=" | ")
        for subject in self.subject:
            print(f"{subject.name}".ljust(12), f"{subject.marks.rounded()}".rjust(12), sep=" | ")


class InternalResult(BaseResult):

    # Already overriding the __init__
    def __init__(self, institute_name: str, title: str, subject: list[Subject]):
        super().__init__(title, subject)
        self.institute_name = institute_name


    def print_result(self):
        print(f"Institute: {self.institute_name}".center(30, "-"))
        super().print_result()
        print("-" * 30)
        print(f"Total Marks:".rjust(12), f"{self.get_total_marks()}".rjust(12), sep=" | ")

    def get_total_marks(self):
        return sum([sub.marks.value for sub in self.subject])


class Result(BaseResult):
    pass


def main():
    subject = [Subject("Maths", Marks(89)), Subject("Science", Marks(90)), Subject("English", Marks(70)), Subject("History", Marks(80))]
    result = InternalResult("XYZ", "Internal", subject)
    result.print_result()

if __name__ == "__main__":
    main()