
from abc import ABC, abstractmethod
from _2_Ride import ride_request, ride_matching


class User( ABC ):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0


    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    


class Rider( User ):
    def __init__(self, name, email, nid, current_location, initial_amount):
        self.current_ride = None
        self.current_location = current_location
        self.wallet = initial_amount
        super().__init__(name, email, nid)


    def display_profile(self):
        print(f'\tRider Name: {self.name}\n\tRider Email: {self.email}\n\tCurrent Location: {self.current_location}')


    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print(' * Invalid Amount * ')

    
    def update_location(self, current_location):
        self.current_location = current_location


    def request_ride(self, ride_sharing, destination, vehicle_type):
        ride_request = ride_request(self, destination)
        ride_matching = ride_matching(ride_sharing.drivers)
        ride = ride_matching.find_driver(ride_request, vehicle_type)
        ride.rider = self
        self.current_ride = ride
        print("YAY!! We got a ride")


    def show_current_ride(self):
        print(f' * {self.current_ride} * ')





class Driver( User ):
    def __init__(self, name, email, nid, current_location):
        self.current_location = current_location 
        self.wallet = 0
        super().__init__(name, email, nid)


    def display_profile(self):
        print(f'\tDriver Name: {self.name}\n\tDiver Email: {self.email}\n\tCurrent Location: {self.current_location}')


    def accept_ride(self, ride):
        ride.set_driver(self)


