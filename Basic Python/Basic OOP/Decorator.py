
def outer_function():
    def inner_function():
        print('Inner Function Started')

        print('Inner FUnction Stop')

    return inner_function


outer_function()()
"""
Inner Function Started
Inner FUnction Stop
"""


# -------------------------------

def outer_function(func):
    def inner_function():
        print('Inner Function Started')
        print(func)
        print('Inner FUnction Stop')

    return inner_function



def time():
    print('Time Started')



# -------------------------------

outer_function(time)()
"""
Inner Function Started
<function time at 0x0000024031A63CE0>
Inner FUnction Stop
"""


# ->

def outer_function(func):
    def inner_function():
        print('Inner Function Started')
        func()
        print('Inner FUnction Stop')

    return inner_function



def time():
    print('Time Started')


outer_function(time)()
"""
Inner Function Started
Time Started
Inner FUnction Stop
"""




# -------------------------------


def outer_function():
    def inner_function():
        print('Inner Function Started')
        
        print('Inner FUnction Stop')

    return inner_function


@outer_function
def time():
    print('Time Started')


outer_function()
"""
Traceback (most recent call last):
  File "e:\Practice\Temp.py", line 11, in <module>
    @outer_function
     ^^^^^^^^^^^^^^
TypeError: outer_function() takes 0 positional arguments but 1 was given
"""



# Solve

def outer_function(func):
    def inner_function():
        print('Inner Function Started')
        func()
        print('Inner FUnction Stop')

    return inner_function


@outer_function
def time():
    print('Time Started')


time()
"""
Inner Function Started
Time Started
Inner FUnction Stop
"""




# -------------------------------
import time

def outer_function(func):
    def inner_function():
        print('Inner Function Started')
        func()
        print('Inner FUnction Stop')

    return inner_function


@outer_function
def Time(something):
    print('Time Started')
    print(something)
    print('Time Ended')


Time( time.ctime() )
"""
Traceback (most recent call last):
  File "e:\Practice\Temp.py", line 20, in <module>
    Time( time.ctime() )
    ~~~~^^^^^^^^^^^^^^^^
TypeError: outer_function.<locals>.inner_function() takes 0 positional arguments but 1 was given
"""



# Solve

def outer_function(func):
    def inner_function(SomeThing):
        print('Inner Function Started')
        func(SomeThing)
        print('Inner FUnction Stop')

    return inner_function


@outer_function
def Time(something):
    print('Time Started')
    print(something)
    print('Time Ended')


Time( time.ctime() )
"""
Inner Function Started
Time Started
Fri Apr 18 21:59:10 2025
Time Ended
Inner FUnction Stop
"""





# ------------------------------- Best Practice

import math
import time
def timer (func):
    def inner(*args, **kwargs):
        print('time started')

        start = time.time()
        func(*args, **kwargs)
        print('time ended')
        end = time.time()

        print(f'total time taken{end-start}')
        
    return inner 


@timer
def get_factorial(n):
    print('factorial starting')
    result = math.factorial(n)
    print(f' factorial of {n} is: {result}')


get_factorial(n=1200)

"""
time started
factorial starting
 factorial of 1200 is: 63507..........
time ended
total time taken0.00022411346435546875

"""
