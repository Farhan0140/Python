class Car:

    # Static attribute (shared by all instances)
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand      # Instance attribute
        self.model = model      # Instance attribute
        Car.total_cars += 1     # Increment static attribute


    # Static method: doesn't access instance (self) or class (cls)
    @staticmethod
    def car_info():
        return "Cars are vehicles used for transportation."
    

    # Class method: works with class, not instance
    @classmethod
    def get_total_cars(cls):
        return f"Total cars created: {cls.total_cars}"
    



# Creating instances
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Accessing static method (can be used without creating an object)
print(Car.car_info())  # Output: Cars are vehicles used for transportation.

# Accessing class method
print(Car.get_total_cars())  # Output: Total cars created: 2

# Accessing static attribute
print(Car.total_cars)  # Output: 2






#
