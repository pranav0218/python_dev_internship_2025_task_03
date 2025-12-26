class Employee:
    def __init__(self,emp_id,name,basic_salary):
        self.emp_id=emp_id
        self.name=name
        self.basic_salary=basic_salary
    
class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, basic_salary):
        super().__init__(emp_id, name, basic_salary)
    
    def calculate_hra(self):
        self.hra=0.20*self.basic_salary
        return self.hra
    
    def calculate_da(self):
        self.da=0.10*self.basic_salary
        return self.da
    
    def total__salary(self):
        self.total_salary=self.basic_salary*self.hra*self.da
        return self.total_salary
    
    def display(self):
        print(f"Employee ID:{self.emp_id}")
        print(f"Employee Name:{self.name}")
        print(f"Employee Basic Salary:{self.basic_salary}")
        print(f"Employee Total Salary:{self.total_salary}")

emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))
obj=SalaryEmployee(emp_id,name,basic_salary)
hra=obj.calculate_hra()
print(hra)
da=obj.calculate_da()
print(da)
obj.total__salary()
obj.display()
