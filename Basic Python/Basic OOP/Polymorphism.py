
# Polymorphism = Greek word that means to "have many forms or faces"

# poly --> many (multiple)
# morph --> shape


# TWO WAYS TO ACHIEVE POLYMORPHISM
# 1. Inheritance = An object could be treated of the same type as a parent class
# 2. "Duck typing" = Object must have necessary attributes/methods

#__________________________________________________________________




from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5



class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping



shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]



for shape in shapes:
    print(f"{shape.area()} cm²")     #  cm ^ 2 ---> 'Alt' + 0178








# _______________________________________________________________________





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




# --------------------------------------------