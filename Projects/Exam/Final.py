# Github Link: https://github.com/Farhan0140/Python/blob/main/Projects/Exam/Final.py


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price




class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, product):
        if product.name.lower() in self.items:
            print(' * Product Already Available * ')
        else:
            self.items[product.name.lower()] = product.price
            print(' * Product Added Successful * ')

    def remove_item(self, product):
        if product.lower() in self.items:
            del self.items[product.lower()]
            print(' * Product Removed Successful * ')
        else:
            print(' * Product Not Found * ')

    def update_price(self, product, new_price):
        if product.lower() in self.items:
            self.items[product.lower()] = new_price
            print(' * Price Updated Successfully * ')
        else:
            print(' * Product Not Found * ')

    def show_menu(self):
        print(f'\n--- Restaurant Menu ---')
        for product, price in self.items.items():
            print(f'-- {product.capitalize()}: ${price}')
        print()




class Order:
    def __init__(self):
        self.total_price = 0.0
        self.orders = {}

    def find_item(self, product_name):
        for item, price in self.orders.items():
            if item.lower() == product_name.lower():
                p_obj = Product(item, price)
                return p_obj
        return None

    def add_to_cart(self, product):
        if product.name.lower() in self.orders:
            self.total_price += product.price
            print(' * Food Successfully Served your table * ')
        else:
            self.orders[product.name.lower()] = product.price
            self.total_price += product.price
            print(' * Food Successfully Served your table * ')

    def place_order(self, balance):
        print(f'Your Available Balance is: {balance}\nand Total Balance is: {self.total_price}')
        if self.total_price <= balance:
            new_balance = balance -self.total_price
            self.total_price = 0.0
            self.orders = {}
            print(f' * Bill Payed Successfully * ')
            return new_balance
        else:
            print(f'Insufficient Balance Please Add More ${self.total_price - balance}') 

    def show_previous_order(self):
        print(f'\n--- Previous Orders ---')
        for product, price in self.orders.items():
            print(f'-- {product.capitalize()}: ${price}')
        print(f'Total price: {self.total_price}\n')




class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.balance = 0
        self.orders = Order()

    def find_item(self, restaurant, product_name):
        for item, price in restaurant.menu.items.items():
            if item.lower() == product_name.lower():
                p_obj = Product(item, price)
                return p_obj
        return None

    def add_to_cart(self, restaurant, product_name):
        product = self.find_item(restaurant, product_name)
        if product:
            self.orders.add_to_cart(product)
        else:
            print(' * Product Not Found in Menu... [Try Again] * ')

    def add_funds(self, amount):
        self.balance += amount
        print(' * Balance Updated Successfully * ')
    
    def check_balance(self):
        return self.balance

    def place_order(self):
        self.balance = self.orders.place_order(self.balance)

    def view_cart(self):
        self.orders.view_cart()

    def view_menu(self, restaurant):
        restaurant.show_menu()

    def show_previous_orders(self):
        self.orders.show_previous_order()




class Admin:
    def __init__(self, name):
        self.name = name

    def add_customer(self, restaurant, person):
        restaurant.add_customer(person)

    def remove_customer(self, restaurant, person_name, person_email):
        restaurant.remove_customer(person_name, person_email)

    def view_customers(self, restaurant):
        restaurant.show_all_customer_info()
    
    def add_item(self, restaurant, product):
        restaurant.add_item(product)

    def remove_item(self, restaurant, product_name):
        restaurant.remove_item(product_name)

    def update_price(self, restaurant, product_name, new_price):
        restaurant.update_price(product_name, new_price)

    def show_menu(self, restaurant):
        restaurant.show_menu()




class Restaurant:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.menu = Menu()

    def find_customer(self, person_name, person_email):
        for p in self.customers:
            if p.email == person_email and p.name.lower() == person_name.lower():
                return p
        return None

    def add_customer(self, person):
        for p in self.customers:
            if p.email == person.email:
                print(' * There is a person who has the same email address. Please choose another one * ')
                return    
        self.customers.append(person)
        print(' * Person Added Successfully * ')

    def remove_customer(self, person_name, person_email):
        for p in self.customers:
            if p.email == person_email and p.name.lower() == person_name.lower():
                print(f' * {person_name} removed successfully * ')
                self.customers.remove(p)
                return
        print('\"\"\"\n  Person Not Found\n  Please provide correct Name and Email\n\"\"\"')

    def show_all_customer_info(self):
        print('\n * --- All Customers --- * ')
        for person in self.customers:
            print(f'-- Name: {person.name.capitalize()}, Email: {person.email}, Address: {person.address.capitalize()} ..')
        print()

    def add_item(self, product):
        self.menu.add_item(product)

    def remove_item(self, product_name):
        self.menu.remove_item(product_name)

    def update_price(self, product_name, new_price):
        self.menu.update_price(product_name, new_price)

    def show_menu(self):
        self.menu.show_menu()

    













admin = Admin('Admin')
res = Restaurant('Sugondha')



def Admin__(a_name):
    print(f'\nWelcome Admin {a_name}\n')

    while True:
        try:
            check = int(input('\n1. Create Customer Account\n2. Remove Customer Account\n3. View All Customer\n4. Manage Restaurant Menu\n5. Exit\n--> '))

            if check == 1:

                p_name = input('Enter Customer Name: ')
                p_email = input('Enter Customer Email: ')
                p_address = input('Enter Customer Address: ')
                p_name = p_name.lower()
                p_email = p_email.lower()
                p_address = p_address.lower()
                new_customer = Customer(p_name, p_email, p_address)
                admin.add_customer(res, new_customer)

            elif check == 2:

                p_name = input('Enter Customer Name: ')
                p_email = input('Enter Customer Email: ')
                p_name = p_name.lower()
                p_email = p_email.lower()
                admin.remove_customer(res, p_name, p_email)
            elif check == 3:
                admin.view_customers(res)

            elif check == 4:
                while True:
                    check_1 = int(input('\n1. Add Item\n2. Remove Item\n3. Update Price\n4. Show Menu\n5. Exit\n--> '))
                    if check_1 == 1:
                        p_name = input('Enter Product Name: ')
                        p_price = int(input('Enter Product Price: '))
                        new_p = Product(p_name, p_price)
                        admin.add_item(res, new_p)
                    elif check_1 == 2:
                        p_name = input('Enter Product Name: ')
                        admin.remove_item(res, p_name)
                    elif check_1 == 3:
                        p_name = input('Enter Product Name: ')
                        p_price = int(input('Enter New Product Price: '))
                        admin.update_price(res, p_name, p_price)
                    elif check_1 == 4:
                        admin.show_menu(res)
                    else:
                        break

            elif check == 5:
                break
            else:
                print('Invalid Input')

        except ValueError:
            print(f'Error: {ValueError}')
        except Exception:
            print(f'An unexpected error occurred {Exception}')



def Customer__(customer):
    print(f'\nWelcome {customer.name}\n')

    while True:
        try:
            check = int(input('\n1. View Restaurant Menu\n2. View Balance\n3. Add Balance\n4. Place Order\n5. Pay Bill\n6. View Past Orders\n7. Exit\n--> '))

            if check == 1:
                customer.view_menu(res)

            elif check == 2:
                print(f'Current Balance is: {customer.check_balance()}')

            elif check == 3:
                c_balance = int(input('Enter amount to add balance to wallet: '))
                customer.add_funds(c_balance)

            elif check == 4:
                p_name = input('Enter Food name: ')
                customer.add_to_cart(res, p_name)
                while True:
                    print('Sir/ma\'am, do you want to try another dish')
                    chk = input('[y/n] ')
                    if chk.lower() == 'y':
                        p_name = input('Enter Food name: ')
                        customer.add_to_cart(res, p_name)
                    else:
                        break
            elif check == 5:
                customer.place_order()
            elif check == 6:
                customer.show_previous_orders()
            elif check == 7:
                break
            else:
                print('Invalid Input')

        except ValueError:
            print(f'Error: {ValueError}')
        except Exception:
            print(f'An unexpected error occurred {Exception}')


#-------------------------------------------------------------------------------------------

while True:
    print('--- Restaurant Management System --- ')
    try:
        check = int(input('1. Admin Login.\n2. Customer Login.\n3. Exit\nSelect an option: ')) 
        if check == 1:
            a_name = input('Enter Admin name: ')
            if a_name.lower() == 'admin':
                Admin__(a_name)
            else:
                print('Try again')
        elif check == 2:
            p_name = input('Enter Customer Name: ')
            p_email = input('Enter Customer Email: ')
            p_name = p_name.lower()
            p_email = p_email.lower()
            customer = res.find_customer(p_name, p_email)

            if customer:
                Customer__(customer)
            else:
                print('\"\"\"\n  Person Not Found\n  Please provide correct Name and Email\n\"\"\"')

    except ValueError:
        print(f'Error: {ValueError}')
    except Exception:
        print(f'An unexpected error occurred: {Exception}')

