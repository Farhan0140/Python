

import _5_Menu as mnu



class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = mnu.Menu()

    
    def find_user(self, user_name):
        for employee in self.employees:
            if employee.name.lower() == user_name.lower():
                return employee
        
        return None


    def add_employee(self, employee):
        self.employees.append( employee )
        print(f' * { employee.name } is added successfully the list * ')


    def remove_employee(self, emp_name):
        employee = self.find_user(emp_name)

        if employee:
            self.employees.remove(employee)
            print(f' * { emp_name } is removed successfully from the list * ')
        else:
            print(f' * {emp_name} Not Found * ')


    def view_employees(self):
        for i, obj in enumerate(self.employees):
            print( f'{i+1} --> Name: {obj.name}  \n      Age: {obj.age} \n      Phone: {obj.phone} \n      Email: {obj.email} \n      Address: {obj.address} \n      Salary: {obj.salary} \n      Designation: {obj.designation} \n      Join Date: {obj.join_date}' )
        print()
