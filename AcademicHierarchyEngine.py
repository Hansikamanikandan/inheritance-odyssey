
class Department:
    def getdeptdetails(self):
        self.id = input("Enter Department ID: ")
        self.name = input("Enter Department Name: ")

    def printdept(self):
        print("\n--- Department Details ---")
        print("Department ID :", self.id)
        print("Department Name :", self.name)

class Course(Department):
    def getcourse(self):
        self.code = input("Enter Course Code: ")
        self.cname = input("Enter Course Name: ")
        self.duration = input("Enter Course Duration: ")

    def printcourse(self):
        print("\n--- Course Details ---")
        print("Course Code :", self.code)
        print("Course Name :", self.cname)
        print("Duration :", self.duration)

class Student(Course):
    def getdetails(self):
        self.rollno = input("Enter Roll Number: ")
        self.sname = input("Enter Student Name: ")
        self.mark = float(input("Enter Mark: "))

    def printstudent(self):
        print("\n--- Student Details ---")
        print("Roll Number :", self.rollno)
        print("Student Name :", self.sname)
        print("Mark :", self.mark)
s = Student()
s.getdeptdetails()
s.getcourse()
s.getdetails()

s.printdept(s.printcourse()
s.printstudent()
