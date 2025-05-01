

class Ticket:
    def __init__(self):
        self.total_price = 0.0
        self.sits = {}

    
    def add_ticket(self, movie, sits_no):          # sits = []
        if movie.sits.is_available_sit():
            if movie.sits.available_sits >= sits_no:
                sit_lst = movie.sits.book_sits(sits_no)

                if sit_lst:
                    self.total_price += (movie.ticket_price * len(sit_lst))
                    self.sits[movie] = sit_lst
                    print('--- Sits booked successfully ---')
            else:
                print(f'--- {sits_no} seats are not available! ---')
                print(f' --- {movie.sits.available_sits} are available now --- ')


    def show_ticket_info(self):
        for movie, sit in self.sits.items():
            print(f'-> {movie.name}')
            print(f'Total Price: {self.total_price} ---')
            print('Sit no. -> ', end='')
            for st in sit:
                print(f'[{st[0]} {st[1]}]', end=' ')
            print('\n-----------------------------------------')


    def ticket_price(self):
        return self.total_price




class Orders:
    def __init__(self):
        self.cart = []
        self.past_orders = []
        self.total_price = 0.0
        self.discount_price = 0.0


    def add_to_cart(self, ticket):
        self.total_price += ticket.ticket_price()
        self.cart.append(ticket)


    def add_coupon(self, cinema_hall, coupon_code):
        x = cinema_hall.find_coupon(coupon_code)

        if x == 0:
            print('--- Coupon Not Available ---')
        else:
            discount_amount = self.total_price * ( x / 100)
            self.discount_price = discount_amount
            print(f'--- Coupon Updated Successfully, You got {x}% Discount ---')


    def pay_bill(self):
        x = (self.total_price - self.discount_price)

        for ticket in self.cart:
            self.past_orders.append(ticket)
            
        self.total_price = 0
        self.cart = []
        print('--- Payment Successful ---')
        return x


    def view_cart(self):
        t_p = 0.0
        print('\t--- Cart ---')
        for item in self.cart:
            t_p += item.ticket_price()
            item.show_ticket_info()
        print(f'- Total Price: {t_p}')


    def view_past_orders(self):
        print('\t--- Previous Orders ---')
        for item in self.past_orders:
            item.show_ticket_info()



