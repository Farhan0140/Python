

import _1_User as usr
import time


class Employee( usr.User ):
    def __init__(self, name, age, phone, email, address, salary, designation):
        self.age = age
        self.salary = salary
        self.designation = designation
        self.join_date = time.ctime()
        super().__init__(name, phone, email, address)

