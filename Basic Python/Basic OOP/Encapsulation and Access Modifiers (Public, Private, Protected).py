# encapsulation --> hide details
# access modifier: public, protected, private


class Bank:
    def __init__ (self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name  # public attribute
        self._branch = 'banani 11'  # protected
        self.__balance = initial_deposit    #   (  __  )---> Private

    def deposit(self, amount):
        self.__balance += amount 
    
    

n = Bank('Farhan Nadim', 1000)
print(n.holder_name)
print(n.__balance)

"""
Traceback (most recent call last):
  File "e:\Practice\Temp.py", line 14, in <module>
    print(n.__balance)
          ^^^^^^^^^^^
AttributeError: 'Bank' object has no attribute '__balance'
"""



# ------------>

class Bank:
    def __init__ (self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name  #   public attribute
        self._branch = 'banani 11'  # protected
        self.__balance = initial_deposit    #   (  __  )---> Private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance   
    
    

n = Bank('Farhan Nadim', 1000)
print(n.holder_name)
print(n.get_balance())  #   1000


# ------------>

print(dir(n))

"""
['_Bank__balance', '__class__', '__delattr__', '__dict__', '__dir__', 
'__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', 
'__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
'__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', 
'__weakref__', 'branch', 'deposit', 'get_balance', 'holder_name']

"""

# ------------> Without get_balance Method
print(n._Bank__balance) #   1000

