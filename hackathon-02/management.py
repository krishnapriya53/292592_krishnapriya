import json
#create class person
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
 
    def get_details(self):
        return (f"name: {self.name}, age: {self.age}, gender: {self.gender}")

#create class employeee inherit from person 
class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary
 
    #get details method
    def get_details(self):
        
        return (f"{super().get_details()}, emp_id: {self.emp_id}, "
                f"Department: {self.department}, Salary: {self.salary}")
    #string representation

    def __str__(self):
        return self.name,self.age,self.gender,self.emp_id,self.department,self.salary
    #fn to salary<50000
    def is_eligible_for_bonus(self):

        return self.salary < 50000
    #cls method 
 
    def from_string(cls, data_string):
        name, age, gender, emp_id, dep, salary = data_string.split(",")
        return cls(name, int(age), gender, emp_id, dep, float(salary))
    from_string = classmethod(from_string)
    #static method
    def bonus_policy():
        print("____Company Bonus Policy____")
        print("-> Employees with salary less than INR 50000 is eligible for BONUSES")
    bonus_policy = staticmethod(bonus_policy)
    
#create class department
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
 
    def add_employee(self, employee):
        self.employees.append(employee)
 
    def get_average_salary(self):
        if not self.employees:
            return 0
        total_salary = sum(emp.salary for emp in self.employees)
        return total_salary / len(self.employees)
 
    def get_all_employees(self):
        return self.employees
 #save to json file
    def save_to_json(self, filename):
        data = []
        for emp in self.employees:
            data.append({
                "name": emp.name,
                "age": emp.age,
                "gender": emp.gender,
                "emp_id": emp.emp_id,
                "department": emp.department,
                "salary": emp.salary
            })
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
 
 #save load 
    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        self.employees = []
        for emp_data in data:
            emp = Employee(
                name=emp_data['name'],
                age=emp_data['age'],
                gender=emp_data['gender'],
                emp_id=emp_data['emp_id'],
                department=emp_data['department'],
                salary=emp_data['salary']
            )
            self.add_employee(emp)
 
# Global functions to support sample-usage.py
def save_to_json(employees, filename="employees.json"):
    data = []
    for emp in employees:
        data.append({
            "name": emp.name,
            "age": emp.age,
            "gender": emp.gender,
            "emp_id": emp.emp_id,
            "department": emp.department,
            "salary": emp.salary
        })
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
 
def load_from_json(filename="employees.json"):
    with open(filename, 'r') as f:
        data = json.load(f)
    employees = []
    for emp_data in data:
        emp = Employee(
            name=emp_data['name'],
            age=emp_data['age'],
            gender=emp_data['gender'],
            emp_id=emp_data['emp_id'],
            department=emp_data['department'],
            salary=emp_data['salary']
        )
        employees.append(emp)
    return employees
 
 