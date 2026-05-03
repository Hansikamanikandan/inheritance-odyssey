class Employee:
    def __init__(self, id, name, salary, percentage):
        self.id = id
        self.name = name
        self.salary = salary
        self.percentage = percentage

    def Calculate_bonus(self):
        return (self.salary * self.percentage) / 100


class Manager(Employee):
    def __init__(self, id, name, salary, percentage,
                 department, team_size, allowance):
        super().__init__(id, name, salary, percentage)
        self.department = department
        self.team_size = team_size
        self.allowance = allowance

    def printManager(self):
        print("\nManager:", self.name)
        print("Department:", self.department)
        print("Bonus:", self.Calculate_bonus())


class Developer(Employee):
    def __init__(self, id, name, salary, percentage,
                 project, experience):
        super().__init__(id, name, salary, percentage)
        self.project = project
        self.experience = experience

    def printDeveloper(self):
        print("\nDeveloper:", self.name)
        print("Project:", self.project)
        print("Bonus:", self.Calculate_bonus())


print("\nEnter Manager Details")
m = Manager(
    input("ID: "),
    input("Name: "),
    float(input("Salary: ")),
    float(input("Bonus %: ")),
    input("Department: "),
    int(input("Team Size: ")),
    float(input("Allowance: "))
)

print("\nEnter Developer Details")
d = Developer(
    input("ID: "),
    input("Name: "),
    float(input("Salary: ")),
    float(input("Bonus %: ")),
    input("Project: "),
    int(input("Experience: "))
)

m.printManager()
d.printDeveloper()
