class Employee:
    db = {}
    def __init__(self,emp_id,emp_name,salary, dept):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
        self.dept = dept

    def add_employee(self):
        val = [self.emp_name, self.salary, self.dept]
        Employee.db[self.emp_id] = val
    
    def get_employee(self,emp_id):
        return Employee.db[emp_id]
    
    def set_salary_change(self, emp_id, salary):
    # Access the employee details by emp_id and update the salary
        if emp_id in Employee.db:
            Employee.db[emp_id][1] = salary  # Update the second element, which is the salary
        else:
            print("Employee ID not found.")



    def get_details(self):
        for key, val in Employee.db.items():
            print(key, val)

class Manager(Employee):
    '''def __init__(self,manager_id):
        super().__init__(emp_id,emp_name,salary, dept)
        self.manager_id = manager_id
        pass'''
    pass
emp1 = Employee(1,'jenish',1000000,'AIML')
emp2 = Employee(2,'Ben',190000,'Mechatronics')

emp1.add_employee()
emp2.add_employee()

print(emp1.get_employee(1))
emp1.get_details()

emp1.set_salary_change(1,50)
print(emp1.get_employee(1))
