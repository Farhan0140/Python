from abc import ABC, abstractmethod
#    abstract base class


class Animal(ABC):

    @abstractmethod #enforce all derived class to have a eat method
    def eat(self):
        pass

    def move(self):
        pass


class Monkey (Animal):
    def __init__ (self, name) -> None:
        self.category = 'Monkey'
        self.name = name
        super().__init__()



Mon = Monkey('Banor')
print(Mon.eat())

"""
e:\Practice\Temp.py:25: SyntaxWarning: invalid escape sequence '\P'

Traceback (most recent call last):
  File "e:\Practice\Temp.py", line 22, in <module>
    Mon = Monkey('Banor')
TypeError: Can't instantiate abstract class Monkey without an implementation for abstract method 'eat'
"""



# -----------------------------

from abc import ABC, abstractmethod
#    abstract base class


class Animal(ABC):

    @abstractmethod #enforce all derived class to have a eat method
    def eat(self):
        pass

    def move(self):
        pass


class Monkey (Animal):
    def __init__ (self, name) -> None:
        self.category = 'Monkey'
        self.name = name
        super().__init__()

    def eat(self):
        return f'I love Banana'


Mon = Monkey('Banor')

print(Mon.eat())    #   I love Banana
