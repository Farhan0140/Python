
import datetime


class RideSharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []


    def add_rider(self, rider):
        self.riders.append(rider)


    def add_driver(self, driver):
        self.drivers.append(driver)

        
    def __str__(self):
        return f"Company Name {self.company_name} with riders : {len(self.riders)} and Drivers : {len(self.drivers)}"




class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.rider = None
        self.driver = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None


    def set_driver(self, driver):
        self.driver = driver


    def start_ride(self):
        self.start_time = datetime.datetime.now()


    def end_ride(self):
        self.end_time = datetime.datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare


    def __repr__(self):
        return f' * Ride Details: *\n\tIt took {self.end_time - self.start_time} hours to get from {self.start_location} to {self.end_location}. '



class ride_request:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location - end_location





class ride_matching:
    def __init__(self, drivers):
        self.available_drivers = drivers


    def find_driver(self, ride_request):
        if len( self.available_drivers ) > 0:
            print('Looking for drivers .........')

            driver = self.available_drivers[0]


            ride = Ride(ride_request.current_location, ride_request.end_location)
            driver.accept_ride(ride)

            return ride


