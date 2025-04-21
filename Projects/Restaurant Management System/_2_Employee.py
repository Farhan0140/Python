

import _1_User as usr
import time


class Employee( usr.User ):
    def __init__(self, name, age, phone, email, address, salary, designation):
        self.age = age
        self.salary = salary
        self.designation = designation
        self.join_date = time.ctime()
        super().__init__(name, phone, email, address)



# new_employee = Employee('Farhan', 23, '01403527730', 'Nadim@gmail.com', 'Dhaka', 20000, 'Junior Software Engineer')
# print(new_employee.__dict__)