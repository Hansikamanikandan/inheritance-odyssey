class Student:
    def __init__(self, name, roll_no, testMark):
        self.name = name
        self.roll_no = roll_no
        self.testMark = testMark

    def display(self):
        print("\nName:", self.name)
        print("Roll No:", self.roll_no)


class Literary_Student(Student):
    def __init__(self, name, roll_no, testMark, literary_marks):
        super().__init__(name, roll_no, testMark)
        self.literary_marks = literary_marks


class Sports_Student(Student):
    def __init__(self, name, roll_no, testMark, sports_marks):
        super().__init__(name, roll_no, testMark)
        self.sports_marks = sports_marks


class Lit_Sport_Student(Literary_Student, Sports_Student):
    def __init__(self, name, roll_no, testMark,
                 literary_marks, sports_marks):
        Student.__init__(self, name, roll_no, testMark)
        self.literary_marks = literary_marks
        self.sports_marks = sports_marks

    def total_marks(self):
        return self.testMark + self.literary_marks + self.sports_marks

    def display(self):
        super().display()
        print("Literary Marks:", self.literary_marks)
        print("Sports Marks:", self.sports_marks)
        print("Total Marks:", self.total_marks())


s = Lit_Sport_Student(
    input("Name: "),
    int(input("Roll No: ")),
    float(input("Test Mark: ")),
    float(input("Literary Marks: ")),
    float(input("Sports Marks: "))
)

s.display()
