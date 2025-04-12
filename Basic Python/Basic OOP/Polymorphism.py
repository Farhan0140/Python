# poly --> many (multiple)
# morph --> shape


class Animal:
    def __init__ (self, name) -> None:
        self.name = name

    def make_sound(self):
        print('animal making some sound')
      

class Cat(Animal):
    def __init__ (self, name) -> None:
        super().__init__(name)


don = Cat('Real Don')
don .make_sound()   #   animal making some sound



# -------------------------------->

class Cat(Animal):
    def __init__ (self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('meow meow')


don = Cat('Real Don')
don .make_sound()   #   meow meow





# -------------------------------->

class Dog(Animal):
    def __init__ (self, name) -> None:
        super().__init__ (name)

    def make_sound(self):
        print('Gheu Gheu')


boss = Dog('Boss')
boss.make_sound()   #   Gheu Gheu



# -------------------------------->

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('beh beh beh')



shepard = Dog('Local Shephard')
shepard. make_sound()

mess = Goat('L M')

mess .make_sound()

less = Goat('gora gor')

animals = [don, shepard, mess, less]
for animal in animals:
    animal.make_sound()

"""
meow meow
Gheu Gheu
beh beh beh
beh beh beh
"""








# ------------------------------------------