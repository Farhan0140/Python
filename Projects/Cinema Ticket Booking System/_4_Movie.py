
from _5_Seats import Seats



class Movie:
    def __init__(self, name, director, running_time, release_date, ticket_price):
        self.name = name
        self.director = director
        self.running_time = running_time
        self.release_date = release_date
        self.ticket_price = ticket_price
        self.seats = Seats()


