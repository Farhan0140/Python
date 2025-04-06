
#-------------
arr = 'hi', 'Hello', 'How are you?'
print( type( arr ) )    #   <class 'tuple'>


#-------------
arr1 = ( 'hi', 'Hello', 'How are you?' )
print( type( arr1 ) )    #   <class 'tuple'>


#-------------
arr = ( 'hi', 'Hello', 'How are you?', 'Farhan', 'Nadim' )
print( arr[0] ) #   hi
print( arr[-1] ) #   Farhan
print( arr[:: -1] ) #   ('Nadim', 'Farhan', 'How are you?', 'Hello', 'hi')

if 'Farhan' in arr:
    print( 'Found' )    #   Found


#-------------
for data in arr:
    print( data )

# ->
# hi
# Hello
# How are you?
# Farhan
# Nadim


#------------- with index
for i, data in enumerate( arr ):
    print( i, data )

# ->
# 0 hi
# 1 Hello
# 2 How are you?
# 3 Farhan
# 4 Nadim


#-------------
t = 12345, 54321, 'hello!'
t[0]
# -> 12345

t
# -> (12345, 54321, 'hello!')

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
# -> ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Tuples are immutable:
t[0] = 88888
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
# -> ([1, 2, 3], [3, 2, 1])



#-------------
#-------------
#-------------
#-------------