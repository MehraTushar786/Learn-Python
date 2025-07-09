class Employee: 
    company  = "Rebo AI"
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return f"Employee Name: {self.name}"

    def get_role(self) :
        return "Employee"
    

    @classmethod
    def ChangeCompanyName(cls,newName):
        cls.company = newName

class Manager(Employee):
    
    def __str__(self):
        return f"Manager Name: {self.name}"
    
    def get_role(self):
        return "Manager"
    

class Developer(Employee):
    def __str__(self):
        return f"Developer Name: {self.name}"
    def get_role(self):
        return "Developers"
    

e = Employee("Amit")
m = Manager("Ravi")
d = Developer("Tushar")

# Print original company
print(e.company)  # Rebo AI
print(m.company)  # Rebo AI
print(d.company)  # Rebo AI

# Change the company name via class method
Employee.ChangeCompanyName("Tushar AI")

# Print again to see the updated company name
print(e.company)  # Tushar AI
print(m.company)  # Tushar AI
print(d.company)  # Tushar AI
