
"""
For example, the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.
This feature in Python that allows the same operator to have different meaning according to the context is called operator overloading.

"""
print( 5 + 10 )     #   15
print( '5' + '10' )    #   510

l1 = [1, 3, 4, 9]
l2 = [99, 14, 12]
print( l1 + l2 )    #   [1, 3, 4, 9, 99, 14, 12]



"""

In Python, we can change the way operators work for user-defined types.


Python Special Functions
Class functions that begin with double underscore __ are called special functions in Python.
They are called "double underscore" functions because they have a double underscore prefix and suffix, such as __init__() or __add__().

__init__() - initialize the attributes of the object
__str__() - returns a string representation of the object
__len__() - returns the length of the object
__add__() - adds two objects
__call__() - call objects of the class like a normal function


"""


# Similarly, we can overload other operators as well:
# Addition 

p1 = 56
p2 = 4
print( p1 + p2 )    # 60
print( p1.__add__(p2) ) # 60


# Subtraction 
print( p1 - p2 )    # 52
print( p1.__sub__(p2) ) # 52


# Multiplication 
print( p1 * p2 )    # 224
print( p1.__mul__(p2) ) # 224


# Power 
print( p1 ** p2 )   # 9834496
print( p1.__pow__(p2) ) # 9834496


# Division 
print( p1 / p2 )    # 14.0
print( p1.__truediv__(p2) ) # 14.0


# Floor Division
print( p1 // p2 )   # 14
print( p1.__floordiv__(p2) )    # 14


"""

Addition	          p1 + p2	    p1.__add__(p2)
Subtraction	          p1 - p2	    p1.__sub__(p2)
Multiplication	          p1 * p2	    p1.__mul__(p2)
Power	                  p1 ** p2	    p1.__pow__(p2)
Division	          p1 / p2	    p1.__truediv__(p2)
Floor Division	          p1 // p2	    p1.__floordiv__(p2)
Remainder (modulo)	  p1 % p2	    p1.__mod__(p2)
Bitwise Left Shift	  p1 << p2	    p1.__lshift__(p2)
Bitwise Right Shift	  p1 >> p2	    p1.__rshift__(p2)
Bitwise AND	          p1 & p2	    p1.__and__(p2)
Bitwise OR	          p1 | p2	    p1.__or__(p2)
Bitwise XOR	          p1 ^ p2	    p1.__xor__(p2)
Bitwise NOT	          ~p1	            p1.__invert__()

"""


"""

Less than	                p1 < p2	    p1.__lt__(p2)
Less than or equal to	        p1 <= p2	p1.__le__(p2)
Equal to	                p1 == p2	p1.__eq__(p2)
Not equal to	                p1 != p2	p1.__ne__(p2)
Greater than	                p1 > p2	    p1.__gt__(p2)
Greater than or equal to	p1 >= p2	p1.__ge__(p2)

"""






class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def eat(self):
        print("Eat junk food every day")


class Cricketer( Person ):
    def __init__(self, name, age, weight, height, team):
        self.team = team
        super().__init__(name, age, weight, height)

    def eat(self):
        print("Eat healthy food every day")

    # def __add__(self, other):
    #     return self.height + other.height

    def __mul__(self, other):
        return self.weight * other.weight



p1 = Cricketer('Juari Sakib', 39, 80, 180, 'BD')
p2 = Cricketer('Tamim', 36, 76, 176, 'BD')


# With-out Overloading 

print( p1 + p2 )
"""
Traceback (most recent call last):
  File "e:\Practice\Temp.py", line 31, in <module>
    print( p1 + p2 )
           ~~~^~~~
TypeError: unsupported operand type(s) for +: 'Cricketer' and 'Cricketer'

"""


print( p1 * p2 )    # 6080
print( len( p1 ) )  # 180
print( p1 > p2 )    # True
print( p1 < p2 )    # False








#
