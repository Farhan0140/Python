
# Why do we need Inheritance?

class Laptop:
    def __init__(self, brand, price, color, memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Running laptop: {self.brand}'

    def coding(self):
        return f'learning python and practicing'
    

class Phone:
    def __init__ (self, brand, price, color, dual_sim) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim

    def run(self):
        return f'phone tipa tipi kore'

    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    

class Camera:
    def __init__ (self, brand, price, color, pixel) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.pixel = pixel

    def run(self):
        pass

    def change_lens (self):
        pass



"""

Inheritance allows code reuse by enabling a class to inherit properties and behaviors (methods) 
from another class, reducing duplication and improving maintainability.

"""


"""

base class, parent class, common attribute + functionality class
 ->  derived class, child class, uncommon attribute + functionality class

"""




class Common_Functionalities:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
        pass
    


class Laptop:
    def __init__(self, memory) -> None:
        self.memory = memory

    def coding(self):
        return f'learning python and practicing'
    

class Phone:
    def __init__ (self, dual_sim) -> None:
        self.dual_sim = dual_sim

    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    

class Camera:
    def __init__ (self, pixel) -> None:
        self.pixel = pixel

    def change_lens (self):
        pass




# ---------------------------------------------