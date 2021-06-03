class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def displayEmployee(self):
        print("Name:",self.name, " Salary:", self.__salary)


emp1 = Employee("Ravi", 50000)
emp1.displayEmployee()
print (emp1.name)
print (emp1.__salary)
