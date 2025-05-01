

class Cinema:
    def __init__(self, hall_name, address):
        self.hall_name = hall_name
        self.address = address
        self.coupon_list = {}
        self.admins = []
        self.movies = []
        self.customers = []


    def find_email(self, email, check):
        if check.lower() == 'a':
            for user in self.admins:
                if user.email.lower() == email.lower() :
                    return user
                
        elif check.lower() == 'c':
            for user in self.customers:
                if user.email.lower() == email.lower() :
                    return user

        return None


    def find_using_obj(self, something, check):
        if check.lower() == 'a':
            for user in self.admins:
                if user.email.lower() == something.email.lower():
                    return user
                
        elif check == 'c':
            for user in self.customers:
                if user.email.lower() == something.email.lower():
                    return user
                
        elif check.lower() == 'm':
            for movie in self.movies:
                if movie.name.lower() == something.name.lower():
                    return movie

        return None


    def find_using_name(self, _name, check, password=None):
        if check.lower() == 'a':
            for user in self.admins:
                if user.email.lower() == _name and user.password == password:
                    return user
                
        elif check.lower() == 'c':
            for user in self.customers:
                if user.email.lower() == _name and user.password == password:
                    return user

        elif check.lower() == 'm':
            for movie in self.movies:
                if movie.name.lower() == _name.lower():
                    return movie

        return None


    def add_movie(self, movie):
        movie_obj = self.find_using_obj(movie, 'm')

        if not movie_obj:
            self.movies.append(movie)
            print(f'--- {movie.name} Added Successfully ---')
        else:
            print(f'--- This movie is already on the list --- ')


    def remove_movie(self, movie_name):
        movie = self.find_using_name(movie_name, 'm')

        if movie:
            print(f'--- Movie {movie.name} Removed Successfully ---')
            self.movies.remove(movie)
        else:
            print('--- No movie found with this name ---')


    def update_movie_info(self, movie_name):
        movie = self.find_using_name(movie_name, 'm')

        if movie:
            print('[1] Change Movie Name\n[2] Change Director\n[3] Change Ticket Price')
            chk = int(input('--> '))

            if chk == 1:
                old = movie.name
                m_name = input('Enter new movie name: ')
                movie.name = m_name
                print(f'--- Movie name {old} to {movie.name} changed successfully --- ')
                self.pe()
            elif chk == 2:
                old = movie.director
                m_d_name = input('Enter New Director name: ')
                movie.director = m_d_name
                print(f'--- Movie director {old} to {movie.director} changed successfully --- ')
                self.pe()
            elif chk == 3:
                old = movie.ticket_price
                m_price = float(input('Enter New Price: '))
                self.ticket_price = m_price
                print(f'--- Ticket price {old} to {movie.ticket_price} changed successfully --- ')
                self.pe()
        else:
            print('--- No movie found with this name ---')
                


    def find_coupon(self, code):
        if code in self.coupon_list:
            return self.coupon_list[code]
        else:
            return 0
        

    def add_coupon(self, code, discount_percentage):
        if code not in self.coupon_list:
            self.coupon_list[code] = discount_percentage
            print('--- Coupon Added Successfully ---')
        else:
            self.coupon_list[code] = discount_percentage
            print('--- Coupon Updated ---')


    def remove_coupon(self, code):
        if code not in self.coupon_list:
            print('--- Coupon Not Found ---')
        else:
            del self.coupon_list[code]
            print('--- Coupon Removed ---')


    def view_coupon_list(self):
        print('Code\t\tDiscount')
        for key, val in self.coupon_list.items():
            print(f'- {key}\t\t{val}%')


    def add_admin(self, _admin):
        self.admins.append(_admin)
        print('--- Account Created Successfully ---')


    def add_customer(self, _user):
        self.customers.append(_user)
        print('--- Account Created Successfully ---')


    def remove_customer(self, user_email):
        for user in self.customers:
            if user.email.lower() == user_email.lower():
                self.customers.remove(user)
                print('--- Customer Removed Successfully ---')
                self.pe()
                return
        print('--- Person Not Found, Try again ---')
        self.pe()



    def update_info(self, user):
        print('[1] Change Name\n[2] Change Password')
        chk = int(input('--> '))

        if chk == 1:
            new_name = input('Enter new name: ')
            user.name = new_name
            print('--- Name Changed Successfully ---')
            self.pe()

        elif chk == 2:
            new_pass = input('Enter new password: ')
            user.password = new_pass
            print('--- Password Changed Successfully ---')
            self.pe()



    def print_all_movie_info(self):
        print('_________ Movie\'s _________')
        print()
        for movie in self.movies:
            print(f'Name: {movie.name.capitalize()}\nDirector: {movie.director.capitalize()}\nRunning Time: {movie.running_time}\nRelease Date: {movie.release_date}\nTicket Price: {movie.ticket_price}')
            print('----  ----')


    def print_all_admin_info(self):
        print('_________ Admin\'s _________')
        print()
        for admin in self.admins:
            print(f'Name: {admin.name.capitalize()}\nEmail: {admin.email}\nJoin Date: {admin.join_date}')
            print('----  ----')


    def print_all_customer_info(self):
        print('_________ Customer\'s _________')
        print()
        for customer in self.customers:
            print(f'ID: Name: {customer.name.capitalize()}\nEmail: {customer.email}')
            print('----  ----')


    
    def pe(self):
        input('---> Press \'Enter\' To Exit ')


