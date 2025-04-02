# Type 1 ---- Take the parameter in order( serial wise )
def sum( x, y ):
    return ( x+y )

print(sum( 10, 20 ))   # 30

# ----
def full_name( s1, s2 ):
    f_n = f'Full name is {s1} {s2}'
    return f_n

print( full_name( "Farhan", "Nadim" ) ) #   Full name is Farhan Nadim


#  ---- Take the parameter in order( we define )
def full_name_2( first, last ):
    f_n = f'Full name is {first} {last}'
    return f_n

print( full_name_2( last='Nadim', first='Farhan' ) ) #   Full name is Farhan Nadim



# Type 2
def d_sum( x, y, z=0 ):    # x, y, and z are its parameters (with z having a default value of 0).
    return ( x + y + z )

print( d_sum(1, 2) )   # 3
print( d_sum(1, 2, 3) )   # 6




# Type 3
def n_sum( *args ):
    sum = 0

    for val in args:
        sum += val
        
    return sum

print( n_sum(1, 2, 3, 4, 5) )   # 15
print( n_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) )    # 55



# Type 4   --- Key Value
def name(first, last, **additional):
    return f'{first} {last} {additional['title']}'

f_name = name(first='Farhan', last='Nadim', title='Bolod')  #   Farhan Nadim Bolod
print(f_name)


# --------
def Key_Value( **kargs):
    for key, val in kargs.items():
        print(key, val)


Key_Value( a=100, b=200, c=00, d=10, e='Farhan') 
# --->
# a 100
# b 200
# c 0
# d 10
# e Farhan




# -------
def all_in_1(x, y, *args, **kargs):
    print(x, y)

    print('*args: ', end="")
    for val in args:
        print(val, end=" ")

    print('\n**kargs: ')
    for key,val in kargs.items():
        print(key, val)


all_in_1(10, 20, 'a', 'b', 'c', 'la', a='a', b='B', c="D")
# ----->
# 10 20
# *args: a b c la 
# **kargs: 
# a a
# b B
# c D



# Type 4   --- return multiple value
def return_multiple( x, y ):
    sum = x + y
    sub = x - y
    mul = x * y
    div = x / y
    rem = x % y

    # return sum, sub, mul, div, rem
    return [sum, sub, mul, div, rem]

all_in_one = return_multiple( 10, 2 )
# print(all_in_one)   #   (12, 8, 20, 5.0, 0)
print(f'Inside Function.py : {all_in_one}')   #   Inside Function.py : [12, 8, 20, 5.0, 0]

