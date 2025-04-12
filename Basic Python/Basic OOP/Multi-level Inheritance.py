

class Vehicle:
    def __init__ (self, name, price) -> None:
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Bus Name: {self.name}, '

    def move(self):
        pass



class Bus(Vehicle):
    def __init__ (self, name, price, seat) -> None:
        self.seat = seat
        super().__init__ (name, price)

    def __repr__(self):
        # return f'Seat: {self.seat}, '
        return super().__repr__()



class Truck(Vehicle):
    def __init__ (self, name, price, weight) -> None:
        self.weight = weight
        super().__init__ (name, price)



class PickUpTruck(Truck):
    def __init__ (self, name, price, weight, speed) -> None:
        self.speed = speed
        super().__init__ (name, price, weight)


class AC_Bus( Bus ):
    def __init__(self, name, price, seat, temperature):
        self.temperature = temperature
        super().__init__(name, price, seat)

    def __repr__(self):
        return super().__repr__()






g_l = AC_Bus('Green Line', 50000000, 30, 26.8)
# print(g_l)  #   Seat: 30, for --> Line 22

print(g_l)  #  Bus Name: Green Line, 






# ----------->