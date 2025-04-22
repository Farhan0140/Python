import os


from _2_Employee import Employee
from _3_Admin import Admin
from _4_Restaurant import Restaurant
from _6_Food_Item import Food_Item
from _7_Customer import Customer





_restaurant_name = input('Enter Restaurant Name: ')
restaurant = Restaurant(_restaurant_name)


def clr_scr():
    os.system('cls' if os.name == 'nt' else 'clear')


def _Customer():
    c_name = input('Enter your name: ')
    c_phone = input('Enter your phone +880')
    c_email = input('Enter your email: ')
    c_address = input('Enter your current address: ')

    _customer = Customer(name = c_name, phone = c_phone, email = c_email, address = c_address)
    

    while(True):
        try:
            clr_scr()
            print(f' *____ Welcome {c_name} ____* ')
            print('1. Show Menu..')
            print('2. Add to Cart..')
            print('3. Remove Item from Cart..')
            print('4. View Cart..')
            print('5. Pay Bill..')
            print('6. Exit..')

            check = int(input('---> '))

            if check == 1:
                clr_scr()
                _customer.show_menu(restaurant)
                check = int(input('Press Enter to exit '))

            elif check == 2:
                clr_scr()
                _customer.show_menu(restaurant)
                _item_name = input('Enter Product name: ')
                _quantity = int(input('Enter Quantity: '))
                _customer.add_to_cart(restaurant, _item_name, _quantity)
                check = int(input('Press Enter to exit '))
            
            elif check == 3:
                clr_scr()
                _customer.view_cart()
                _item_name = input('Enter Product name: ')
                _customer.remove_from_cart(restaurant, _item_name)
                check = int(input('Press Enter to exit '))

            elif check == 4:
                clr_scr()
                _customer.view_cart()
                check = int(input('Press Enter to exit '))

            elif check == 5:
                clr_scr()
                print(f' {_customer.cart.total_price} paid successfully ')
                _customer.cart.clear_orders()
                check = int(input('Press Enter to exit '))

            elif check == 6:
                break
            else:
                print(' * Invalid Input * ')
            
        except ValueError:
            print(f'Error: {ValueError}')
        except Exception:
            print(f"An unexpected error occurred: {Exception}")




def _Admin():
    a_name = input('Enter your name: ')
    a_age = input('Enter your age: ')
    a_phone = input('Enter your phone +880')
    a_email = input('Enter your email: ')
    a_address = input('Enter your current address: ')
    a_designation = input('Enter your Designation: ')

    _admin = Admin(name = a_name, age = a_age, phone = a_phone, email = a_email, address = a_address, designation = a_designation)

    while(True):
        try:
            clr_scr()
            print(f' *____ Welcome {a_name} ____* ')
            print('1. View Employee List..')
            print('2. Add Employee..')
            print('3. Remove Employee..')
            print('4. Show Menu..')
            print('5. Add Item..')
            print('6. Remove Item..')
            print('7. Exit..')

            check = int(input('---> '))

            if check == 1:
                clr_scr()
                _admin.view_employees(restaurant)
                check = int(input('Press Enter to exit '))


            # name, age, phone, email, address, salary, designation):
            elif check == 2:
                clr_scr()
                _emp_name = input('Enter Employee\'s name: ')
                _emp_age = int(input('Enter Employee\'s age: '))
                _emp_phone = input('Enter your phone +880')
                _emp_email = input('Enter Employee\'s Email: ')
                _emp_add = input('Enter Employee\'s Address: ')
                _emp_salary = int(input('Enter Employee\'s Salary: '))
                _emp_designation = input('Enter Employee\'s Designation: ')

                _new_emp = Employee(name=_emp_name, age=_emp_age, phone=_emp_phone, email=_emp_email, address=_emp_add, salary=_emp_salary, designation=_emp_designation)

                _admin.add_employee(restaurant, _new_emp)
                check = int(input('Press Enter to exit '))
            
            elif check == 3:
                clr_scr()
                _emp_name = input('Enter Employee\'s name: ')
                _admin.remove_employee(restaurant, _emp_name)
                check = int(input('Press Enter to exit '))

            elif check == 4:
                clr_scr()
                _admin.show_menu(restaurant)
                check = int(input('Press Enter to exit '))

            elif check == 5:
                clr_scr()
                _itm_name = input('Enter Item Name: ')
                _itm_price = float(input('Enter Product Price: '))
                _itm_quantity = int(input('Enter Product Quantity: '))

                _new_item = Food_Item(name=_itm_name, price=_itm_price, quantity=_itm_quantity)

                _admin.add_item(restaurant, _new_item)
                check = int(input('Press Enter to exit '))

            elif check == 6:
                clr_scr()
                _itm_name = input('Enter Item Name: ')
                _admin.remove_item(restaurant, _itm_name)

            elif check == 7:
                break
            else:
                print(' * Invalid Input * ')
            
        except ValueError:
            print(f'Error: {ValueError}')
        except Exception:
            print(f"An unexpected error occurred: {Exception}")



while True:
    print(f' *____ Welcome {restaurant.name} Resraurant ____* ')
    print('1. Admin Login')
    print('2. Customer Login')
    print('3. Exit')

    try:
        check = int(input('---> '))
        if check == 1:
            clr_scr()
            _Admin()
        elif check == 2:
            clr_scr()
            _Customer()
        elif check == 3:
            break
        else:
            print('Invalid Input')
            
    except ValueError:
        print(f'Error: {ValueError}')
    except Exception:
        print(f"An unexpected error occurred: {Exception}")


