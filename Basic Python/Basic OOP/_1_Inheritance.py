
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
    
    def __repr__(self):
        return f'Has dual SIM: {self.dual_sim}'
    

class Camera:
    def __init__ (self, pixel) -> None:
        self.pixel = pixel

    def change_lens (self):
        pass

"""

Without relation, we can only access


my_phn = Phone(True)
my_phn.phone_call()
print(my_phn)

"""




# -------------------------------------------------------------------------------------




class Common_Functionalities:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
        pass



class Laptop( Common_Functionalities ):
    def __init__(self, brand, price, color, memory):
        self.memory = memory
        super().__init__(brand, price, color)

    def run(self):
        return f'Running laptop: {self.brand}'

    def coding(self):
        return f'learning python and practicing'
    

class Phone( Common_Functionalities ):
    def __init__ (self, brand, price, color, dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand, price, color)

    def run(self):
        return f'phone tipa tipi kore'

    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    
    def __repr__(self):
        return f'Brand: {self.brand}, Color: {self.color}, Price: {self.price}, Has dual SIM: {self.dual_sim}'
    

class Camera( Common_Functionalities ):
    def __init__ (self, brand, price, color, pixel):
        self.pixel = pixel
        super().__init__(brand, price, color)

    def run(self):
        pass

    def change_lens (self):
        pass




my_phn = Phone('Honor', 10000, 'Blue', True)
print(my_phn)


"""
Brand: Honor, Color: Blue, Price: 10000, Has dual SIM: True
"""
