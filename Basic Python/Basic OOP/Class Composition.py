"""
Use inheritance when classes have an “is-a” relationship.
Use composition when classes have a “has-a” or “can-do” relationship.
"""



# Define behavior classes
class CanEat:
    def eat(self):
        print(f"{self.name} is eating")

class CanWalk:
    def walk(self):
        print(f"{self.name} is walking")

class CanSwim:
    def swim(self):
        print(f"{self.name} is swimming")

# Compose behaviors into a new class
class Person:
    def __init__(self, name):
        self.name = name
        self.eater = CanEat()
        self.eater.name = name
        self.walker = CanWalk()
        self.walker.name = name

    def eat(self):
        self.eater.eat()

    def walk(self):
        self.walker.walk()

class Fish:
    def __init__(self, name):
        self.name = name
        self.eater = CanEat()
        self.eater.name = name
        self.swimmer = CanSwim()
        self.swimmer.name = name

    def eat(self):
        self.eater.eat()

    def swim(self):
        self.swimmer.swim()

# Usage
person = Person("Alice")
person.eat()   # Alice is eating
person.walk()  # Alice is walking

fish = Fish("Nemo")
fish.eat()     # Nemo is eating
fish.swim()    # Nemo is swimming




# ______________________________________________________________________

class CPU:
    def __init__ (self, cores) -> None:
        self.cores = cores

        
class RAM:
    def __init__(self, size) -> None:
        self.size = size


class HardDrive:
    def __init__ (self, model, capacity) -> None:
        self.model = model
        self.capacity = capacity


# computer "has a" cpu
# computer "has a" ram
# computer "has a" hard drive
class Computer:
    def __init__ (self, cores, ram_size, hd_capacity, hd_model) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hard_disc = HardDrive(hd_model, hd_capacity)


Windows = Computer(8, 16, 10000, 'Kt-890')

print( Windows.hard_disc.model )



# 