
import _1_User as usr


class Admin( usr.User ):
    def __init__(self, name, age, phone, email, address, designation):
        self.age = age
        self.designation = designation
        super().__init__(name, phone, email, address)


    def add_employee(self, restaurant, employee):
        restaurant.add_employee( employee )


    def remove_employee(self, restaurant, emp_name):
        restaurant.remove_employee(emp_name)
   

    def view_employees(self, restaurant):
        restaurant.view_employees()

    
    def add_item(self, restaurant, item):
        restaurant.menu.add_item(item)

    
    def remove_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)


    def show_menu(self, restaurant):
        restaurant.menu.show_menu()

