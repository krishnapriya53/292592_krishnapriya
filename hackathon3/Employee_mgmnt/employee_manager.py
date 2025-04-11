# employee_manager.py
 
from employee import Employee
 
class EmployeeManager:
    def __init__(self):
        self.employees = []
    #add employee
    def add_employee(self, name, department, designation, gross_salary, tax, bonus):
        employee = Employee(name, department, designation, gross_salary, tax, bonus)
        self.employees.append(employee)
        return employee
    #view all employee
    def get_all_employees(self):
        return self.employees
    #search id
    def find_by_id(self, emp_id):
        for e in self.employees:
            if e.id == emp_id:
                return e
        return None
        
 
    #delete emp
    def delete_employee(self, emp_id):
        employee = self.find_by_id(emp_id)
        if employee:
            self.employees.remove(employee)
            return True
        return False
       
  
    #save and load emp
    def load_employees(self, employee_dicts):
        self.employees = [Employee.from_dict(d) for d in employee_dicts]
 
    def to_dict_list(self):
        return [e.to_dict() for e in self.employees]
 
 