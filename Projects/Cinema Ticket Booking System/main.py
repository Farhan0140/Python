import os


from _2_Admin import Admin
from _3_Cinema import Cinema
from _4_Movie import Movie
from _6_Customer import Customer


def clr_scr():
    os.system('cls' if os.name == 'nt' else 'clear')

def pe():
    input('---> Press \'Enter\' To Exit ')


star_cineplex = Cinema('Star Cineplex', 'Dhaka')
admin = Admin('admin', 'admin', 'admin')
star_cineplex.add_admin(admin)

admin.add_coupon(star_cineplex, 'nostonadim', 10)
admin.add_coupon(star_cineplex, 'starcineplex', 20)

movie1 = Movie('frozen', 'Jennifer Lee, Chris Buck', '1h 42m', 'February 14, 2014', 250.00)
movie2 = Movie('the bad guys', 'Pierre Perifel', '1h 40m', 'April 1, 2022', 300.00)
movie3 = Movie('the secret life of pets', 'Chris Renaud', '1h 26m', 'June 7, 2016', 300.00)
movie4 = Movie('abominable', 'Chris Renaud', '1h 37m', 'April 1, 2019', 300.00)
movie5 = Movie('wish dragon', 'Chris Appelhans', '1h 38m', 'January 15, 2021', 350.00)
star_cineplex.add_movie(movie1)
star_cineplex.add_movie(movie2)
star_cineplex.add_movie(movie3)
star_cineplex.add_movie(movie4)
star_cineplex.add_movie(movie5)

clr_scr()




def authenticate_user(name, email, m_pass, c_pass, a_or_c): #m_pass: main password __ c_pass: confirm password
    
    while m_pass != c_pass:
        c_pass = input('Enter password again: ')

    if a_or_c.lower() == 'a':
        new_admin = star_cineplex.find_email(email, 'a')

        if new_admin:
            print(f'--- This email is already registered. Please login --- ')
            return

        new_admin = Admin(name, email, m_pass)
        star_cineplex.add_admin(new_admin)
    else:
        new_customer = star_cineplex.find_email(email, 'c')
        if new_customer:
            print(f'--- This email is already registered. Please login --- ')
            return

        new_customer = Customer(name, email, m_pass)
        star_cineplex.add_customer(new_customer)

        

def find_user(email, u_pass, a_or_c):
    if a_or_c.lower() == 'a':
        new_admin = star_cineplex.find_using_name(email, 'a', u_pass)
        if new_admin:
            return new_admin
        
        print('Email or Password Don\'t match. Create an account or try again')
        return None
    else:
        new_customer = star_cineplex.find_using_name(email, 'c', u_pass)
        if new_customer:
            return new_customer
        
        print('Email or Password Don\'t match. Create an account or try again')
        return None
    
    

def Customer__(user):
    while True:
        clr_scr()
        print('[1] Update Info\n[2] View Movie List\n[3] Book Ticket\n[4] View Available Seats\n[5] Check Balance\n[6] Cash In\n[7] View Cart\n[8] Pay Bill\n[9] View Previous Orders\n[10] Exit')
        try:
            check = int(input('--->  '))
            if check == 1:
                clr_scr()
                user.update_info(star_cineplex, user)

            elif check == 2:
                clr_scr()
                user.view_movie_list(star_cineplex)
                pe()

            elif check == 3:
                clr_scr()
                user.view_movie_list(star_cineplex)
                m_name = input('Enter Movie Name: ')
                m_seats = int(input('Enter How Many Seats you need: '))
                clr_scr()
                chk = input('[y/n] View Available Seats\n--> ')
                if chk.lower() == 'y':
                    user.view_available_seats(star_cineplex, m_name)
                    user.book_ticket(star_cineplex, m_name, m_seats)
                else:
                    user.book_ticket(star_cineplex, m_name, m_seats)
                pe()
            elif check == 4:
                clr_scr()
                m_name = input('Enter Movie Name: ')
                user.view_available_seats(star_cineplex, m_name)
                pe()
            elif check == 5:
                clr_scr()
                print(f'Available Balance: {user.check_balance()}' )
                pe()
            elif check == 6:
                clr_scr()
                u_amount = float(input('Enter amount to cash-in: '))
                user.add_balance(u_amount)
                pe()
            elif check == 7:
                clr_scr()
                user.view_cart()
                pe()
            elif check == 8:
                clr_scr()
                chk = input('Do you have any coupons [y/n]: ')
                if chk.lower() == 'y':
                    c_code = input('Enter Coupon Code: ')
                    user.add_coupon(star_cineplex, c_code)
                user.pay_bill()
                pe()
            elif check == 9:
                clr_scr()
                user.view_past_orders()
                pe()
            elif check == 10:
                break


        except ValueError:
            print(f'Error: {ValueError}')
        except Exception:
            print(f"An unexpected error occurred: {Exception}")




def Admin__(user):
    while True:
        clr_scr()
        print('[1] Update Info\n[2] Add Movie\n[3] Remove Movie\n[4] Update Movie Info\n[5] Show Movies\n[6] Add Coupon\n[7] Remove Coupon\n[8] View Coupons\n[9] Remove User\n[10] View Customers Info\n[11] Exit')
        try:
            check = int(input('--->  '))
            if check == 1:
                clr_scr()
                user.update_info(star_cineplex, user)

            elif check == 2:
                clr_scr()
                m_name = input('Enter Movie Name: ')
                m_director = input('Enter Director: ')
                m_running_time = input('Enter Running Time: ')
                m_release_date = input('Enter Release Date: ')
                m_ticket_price = float(input('Enter Ticket Price: '))
                movie = Movie(m_name, m_director, m_running_time, m_release_date, m_ticket_price)
                user.add_movie(star_cineplex, movie)
                pe()
            elif check == 3:
                clr_scr()
                m_name = input('Enter Movie Name to Remove: ')
                user.remove_movie(star_cineplex, m_name)
                pe()
            elif check == 4:
                clr_scr()
                m_name = input('Enter Movie Name to Update: ')
                user.update_movie_info(star_cineplex, m_name)
            elif check == 5:
                clr_scr()
                star_cineplex.print_all_movie_info()
                pe()
            elif check == 6:
                clr_scr()
                c_code = input('Enter Coupon Code: ')
                c_dis = input('Enter Discount in (%): ')
                user.add_coupon(star_cineplex, c_code, c_dis)
                pe()
            elif check == 7:
                clr_scr()
                c_code = input('Enter Coupon Code: ')
                user.remove_coupon(star_cineplex, c_code)
                pe()
            elif check == 8:
                clr_scr()
                user.view_coupon(star_cineplex)
                pe()
            elif check == 9:
                clr_scr()
                s_email = input('Enter customer email to remove: ')
                user.remove_user(star_cineplex, s_email)
            elif check == 10:
                clr_scr()
                user.view_users_info(star_cineplex)
                pe()
            elif check == 11:
                break


        except ValueError:
            print(f'Error: {ValueError}')
        except Exception:
            print(f"An unexpected error occurred: {Exception}")


# __________________________________________________________________________________________



while True:
    clr_scr()
    print(f' * ____ Welcome to {star_cineplex.hall_name} ____ * \n')
    try:
        check = input('-> Do you have an account? [y/n/Enter for Exit]: ').lower()

        if check == 'y':
            clr_scr()
            print('Login Account')
            print('1. As a admin\n2. As a customer')
            check = int(input('--->  '))
            if check == 1:
                clr_scr()
                s_email = input('Enter your email: ')
                s_pass = input('Enter your password: ')
                user = find_user(s_email, s_pass, 'a')
                if user:
                    Admin__(user)
                else:
                    input('Press Enter To exit: ')

            elif check == 2:
                clr_scr()
                c_email = input('Enter your email: ')
                c_pass = input('Enter your password: ')
                user = find_user(c_email, c_pass, 'c')
                if user:
                    Customer__(user)
                else:
                    input('Press Enter To exit: ')


        elif check == 'n':
            clr_scr()
            print('Create an account :')
            print('1. As a admin\n2. As a customer')
            check = int(input('--->  '))

            if check == 1:
                clr_scr()
                s_name = input('Enter your name: ')
                s_email = input('Enter your email: ')
                s_pass = input('Enter your password: ')
                c_s_pass = input('Confirm your password: ')

                s_name = s_name.lower()
                s_email = s_email.lower()

                authenticate_user(s_name, s_email, s_pass, c_s_pass, 'a')
                input('Press Enter To exit: ')
            
            elif check == 2:
                clr_scr()
                c_name = input('Enter your name: ')
                c_email = input('Enter your email: ')
                c_pass = input('Enter your password: ')
                c_c_pass = input('Confirm your password: ')

                c_name = c_name.lower()
                c_email = c_email.lower()

                authenticate_user(c_name, c_email, c_pass, c_c_pass, 'c')
                input('Press Enter To exit: ')
        else:
            break

    except ValueError:
        print(f'Error: {ValueError}')
    except Exception:
        print(f"An unexpected error occurred: {Exception}")

