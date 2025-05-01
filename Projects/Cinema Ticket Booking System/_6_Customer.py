
from _1_User import User
from _7_Order import Orders, Ticket


class Customer( User ):
    def __init__(self, name, email, password):
        self.wallet = 0.0
        self.cart = Orders()
        super().__init__(name, email, password)


    def update_info(self, cinema_hall, user):
        cinema_hall.update_info(user)


    def view_movie_list(self, cinema_hall):
        cinema_hall.print_all_movie_info()


    def book_ticket(self, cinema_hall, movie_name, seat_no):
        movie = cinema_hall.find_using_name(movie_name, 'm')
        if movie:
            if (movie.ticket_price * seat_no) <= self.wallet:
                ticket = Ticket()
                ticket.add_ticket(movie, seat_no)
                self.cart.add_to_cart(ticket)
            else:
                print(f'--- Insufficient Balance!! ---')
        else:
            print('--- Movie Not Found ---')


    def add_balance(self, amount):
        if amount > 0:
            self.wallet += amount
            print('--- Cash-in Successfully ---')
            print(f'--- Current Balance is: {self.wallet} ---')
        else:
            print('--- Invalid Amount ---')


    def view_available_seats(self, cinema_hall, movie_name):
        movie = cinema_hall.find_using_name(movie_name, 'm')
        if movie:
            movie.seats.view_seat_map()
        else:
            print('--- Movie Not Found ---')


    def pay_bill(self):
        self.wallet -= self.cart.pay_bill()
        
    
    def add_coupon(self, cinema_hall, coupon_code):
        self.cart.add_coupon(cinema_hall, coupon_code)


    def view_cart(self):
        self.cart.view_cart()


    def view_past_orders(self):
        self.cart.view_past_orders()


    def check_balance(self):
        return self.wallet

