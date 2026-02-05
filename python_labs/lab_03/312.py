class Employee():
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def total_salary(self, name, base_salary):
        return [name, base_salary]

class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent
    def total_salary(self, name, base_salary, bonus_percent):
        return [name, base_salary * (100 + bonus_percent) / 100]

class Developer(Employee):
    def __init__(self, name, base_salary, projects):
        super().__init__(name, base_salary)
        self.projects = projects
    def total_salary(self, name, base_salary, projects):
        return [name, base_salary + projects * 500]
    
class Intern(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)
    def total_salary(self, name, base_salary):
        return super().total_salary(name, base_salary)

employee_info = list(map(str, input().split()))
if employee_info[0] == "Manager":
    name = employee_info[1]
    base_salary = int(employee_info[2])
    bonus_percent = int(employee_info[3])
    emp = Manager(name, base_salary, bonus_percent)
    salary_info = emp.total_salary(name, base_salary, bonus_percent)
    print(f"Name: {salary_info[0]}, Total: {salary_info[1]:.2f}")

elif employee_info[0] == "Developer":
    name = employee_info[1]
    base_salary = int(employee_info[2])
    projects = int(employee_info[3])
    emp = Developer(name, base_salary, projects)
    salary_info = emp.total_salary(name, base_salary, projects)
    print(f"Name: {salary_info[0]}, Total: {salary_info[1]:.2f}")

elif employee_info[0] == "Intern":
    name = employee_info[1]
    base_salary = int(employee_info[2])
    emp = Intern(name, base_salary)
    salary_info = emp.total_salary(name, base_salary)
    print(f"Name: {salary_info[0]}, Total: {salary_info[1]:.2f}")
    

else:
    pass