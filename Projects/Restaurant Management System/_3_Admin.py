
import _1_User as usr
import _2_Employee as emp
import _4_Restaurant as rest
import _6_Food_Item as fd_itm
import _7_Customer as cstmr


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






# _1_rest = rest.Restaurant('Suganda')
# _1st_admin = Admin('Farhan', 23, '123123', 'asdasd@asd.com', 'dhaka', 'CEO')








# _1_f = fd_itm.Food_Item('Pizza', 1200, 10)
# _2_f = fd_itm.Food_Item('Burgir', 600, 5)


# _1st_admin.add_item(_1_rest, _1_f)
# _1st_admin.add_item(_1_rest, _2_f)

# # _1st_admin.remove_item(_1_rest, 'Burgir')

# # _1st_admin.show_menu(_1_rest)

# _1_cstmr = cstmr.Customer('Mitu', '0144545', 'mitu@gmail.com', 'Bosti')
# _1_cstmr.add_to_cart(_1_rest, 'pizza', 3)
# _1_cstmr.add_to_cart(_1_rest, 'burgir', 3)

# _1_cstmr.remove_from_cart(_1_rest, 'burgir')
# # _1_cstmr.remove_from_cart(_1_rest, 'pizza')

# _1_cstmr.view_cart()

# _1st_admin.show_menu(_1_rest)







# emp_1 = emp.Employee('Celia', 28, '1958177', 'fohdepid@gosve.fm', 'Monaco', 16865, 'Chef')
# emp_2 = emp.Employee('Susan', 21, '1943319', 'weowaka@tosuhih.tw', 'Falkland Islands', 49427, 'Cashier')




# _1st_admin.add_employee(_1_rest, emp_1)
# _1st_admin.add_employee(_1_rest, emp_2)

# _1st_admin.remove_employee(_1_rest, 'celia')

# _1st_admin.view_employees(_1_rest)




