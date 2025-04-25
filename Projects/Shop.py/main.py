
from _2_Seller import Seller
from _3_Shop import Shop
from _4_Item import Item
from _5_Customer import Customer


__shop = Shop('Shopno', 'Bhuighar')


sellers = []
customers = []


# __________________________________________________________________________________________


def authenticate_user(name, email, m_pass, c_pass, S_or_C): #m_pass: main password __ c_pass: confirm password
    
    while m_pass != c_pass:
        c_pass = input('Enter password again: ')

    if S_or_C.lower() == 's':
        for seller in sellers:
            if seller.email.lower() == email.lower():
                print(' * Email Already Exist * \n * Give New One * ')
                return

        new_seller = Seller(name, email, m_pass)
        sellers.append( new_seller )
        print(' * Account Created Successfully * ')
    else:
        for customer in customers:
            if customer.email.lower() == email.lower():
                print(' * Email Already Exist * \n * Give New One * ')
                return
            
        new_customer = Customer(name, email, m_pass)
        customers.append(new_customer)
        print(' * Account Created Successfully * ')

        

def find_user(email, u_pass, s_or_c):
    if s_or_c.lower() == 's':
        for user in sellers:
            if user.email == email:
                if user.password == u_pass:
                    return user
                else:
                    print('Password Incorrect. Try again')
                    return None
        
        print('Email Not Found. Create an account and try again')
        return None
    else:
        for user in customers:
            if user.email == email:
                if user.password == u_pass:
                    return user
                else:
                    print('Password Incorrect. Try again')
                    return None
        
        print('Email Not Found. Create an account and try again')
        return None
    
    

def Customer__(user):
    while True:
        print('1. Available Products\n2. Add to Cart\n3. Remove from Cart\n4. View Cart\n5. Pay Bill\n6.Exit')
        try:
            check = int(input('--->  '))
            if check == 1:
                __shop.show_all_products()

            elif check == 2:
                __shop.show_all_products()
                i_name = input('Enter Product Name: ')
                i_quantity = int(input('Enter Product Quantity: '))

                user.add_to_cart(__shop, i_name, i_quantity)
                input('Press Enter To exit: ')

            elif check == 3:
                i_name = input('Enter Product Name: ')
                user.remove_from_cart(__shop, i_name)
                input('Press Enter To exit: ')
                
            elif check == 4:
                user.view_cart()
            elif check == 5:
                user.make_payment()
            elif check == 6:
                break


        except ValueError:
            print(f'Error: {ValueError}')
        except Exception:
            print(f"An unexpected error occurred: {Exception}")




def Seller__(user):
    while True:
        print('1. Add Product\n2. Remove Product\n3. See Products\n4.Exit')
        try:
            check = int(input('--->  '))
            if check == 1:
                i_name = input('Enter Product Name: ')
                i_price = float(input('Enter Product Price: '))
                i_quantity = int(input('Enter Product Quantity: '))
                i_type = input('Enter Selling Type per (kg, pcs): ')

                new_item = Item(i_name, i_price, i_quantity, i_type)
                user.add_product(__shop, new_item)
                input('Press Enter To exit: ')

            elif check == 2:
                i_name = input('Enter Product Name to Remove: ')
                user.remove_product(__shop, i_name)
                input('Press Enter To exit: ')

            elif check == 3:
                user.see_products()
            elif check == 4:
                break


        except ValueError:
            print(f'Error: {ValueError}')
        except Exception:
            print(f"An unexpected error occurred: {Exception}")


# __________________________________________________________________________________________



while True:
    print(f' * ____ Welcome to {__shop.name} SuperShop ____ * \n')
    try:
        check = input('-> Do you have an account? [y/n/Enter for Exit]: ').lower()

        if check == 'y':
            print('Login Account')
            print('1. As a seller\n2. As a customer')
            check = int(input('--->  '))
            if check == 1:
                s_email = input('Enter your email: ')
                s_pass = input('Enter your password: ')
                user = find_user(s_email, s_pass, 's')
                if user:
                    Seller__(user)

                else:
                    input('Press Enter To exit: ')

            elif check == 2:
                c_email = input('Enter your email: ')
                c_pass = input('Enter your password: ')
                user = find_user(c_email, c_pass, 'c')
                if user:
                    Customer__(user)

                else:
                    input('Press Enter To exit: ')



        elif check == 'n':
            print('Create an account :')
            print('1. As a seller\n2. As a customer')
            check = int(input('--->  '))

            if check == 1:
                s_name = input('Enter your name: ')
                s_email = input('Enter your email: ')
                s_pass = input('Enter your password: ')
                c_s_pass = input('Confirm your password: ')

                authenticate_user(s_name, s_email, s_pass, c_s_pass, 's')
                input('Press Enter To exit: ')
            
            elif check == 2:
                c_name = input('Enter your name: ')
                c_email = input('Enter your email: ')
                c_pass = input('Enter your password: ')
                c_c_pass = input('Confirm your password: ')

                authenticate_user(c_name, c_email, c_pass, c_c_pass, 'c')
                input('Press Enter To exit: ')

        else:
            break

            

    except ValueError:
        print(f'Error: {ValueError}')
    except Exception:
        print(f"An unexpected error occurred: {Exception}")




