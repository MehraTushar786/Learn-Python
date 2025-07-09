class Employee: 
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return f"Employee Name: {self.name}"

    def get_role(self) :
        return "Employee"

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
    


# Create objects
e = Employee("Amit")
m = Manager("Ravi")
d = Developer("Tushar")

# Print roles
print(e.get_role())  # Employee
print(m.get_role())  # Manager
print(d.get_role())  # Developer

# Print string representations
print(e)  # Employee: Amit
print(m)  # Manager: Ravi
print(d)  # Developer: Tushar