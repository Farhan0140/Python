import datetime

from _1_User import User



class Admin( User ):
    def __init__(self, name, email, password):
        self.join_date = datetime.datetime.now()
        super().__init__( name, email, password)


    def update_info(self, cinema_hall, user):
        cinema_hall.update_info(user)


    def add_movie(self, cinema_hall, movie):
        cinema_hall.add_movie(movie)


    def remove_movie(self, cinema_hall, movie_name):
        cinema_hall.remove_movie(movie_name)


    def update_movie_info(self, cinema_hall, movie_name):
        cinema_hall.update_movie_info(movie_name)


    def show_movies(self, cinema_hall):
        cinema_hall.print_all_movie_info()


    def add_coupon(self, cinema_hall, coupon_code, discount_percentage):
        cinema_hall.add_coupon(coupon_code, discount_percentage)


    def view_coupon(self, cinema_hall):
        cinema_hall.view_coupon_list()


    def remove_coupon(self, cinema_hall, code):
        cinema_hall.remove_coupon(code)


    def remove_user(self, cinema_hall, user_email):
        cinema_hall.remove_customer(user_email)


    def view_users_info(self, cinema_hall):
        cinema_hall.print_all_customer_info()




