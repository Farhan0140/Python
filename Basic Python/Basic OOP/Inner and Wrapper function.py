

def outer_function():
    print('Outer Function Start')

    def inner_function():
        print('Inner Function')

    return inner_function


print( outer_function() )   
"""
Outer Function Start
<function outer_function.<locals>.inner_function at 0x000001FD6A223CE0>
""" 


print( outer_function()() )
"""
Outer Function Start
Inner Function
None
"""


# If inner function return anything

def outer_function():
    print('Outer Function Start')

    def inner_function():
        print('Inner Function')
        return 'Returned from inner function'

    return inner_function

 


print( outer_function()() )
"""
Outer Function Start
Inner Function
Returned from inner function
"""




# ___________________________________________________________________


def do_somthing(work):
    print('Reading')
    print(work)
    work()
    print('Reading End')


# -------------------
do_somthing('Book')
"""
Reading
Book
Reading End
"""


# -------------------
def python():
    print('Coding in python')


do_somthing(python)
"""
Reading
<function python at 0x000002CA56393CE0>
Reading End
"""


# -------------------
def c():
    print('Coding in C')


do_somthing(c)
"""
Reading
<function c at 0x00000280D70C3E20>
Coding in C
Reading End
"""





# -------------------