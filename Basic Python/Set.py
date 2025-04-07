# ---> {}

# ----------
arr = [1, 65, 2, 3, 1, 1, 1, 34, 3, 3, 2]
print( arr )    #   [1, 65, 2, 3, 1, 1, 1, 34, 3, 3, 2]

st = set( arr )
print( st ) #   {65, 1, 2, 3, 34}


# ----------
st.add(99)
print( st ) #   {65, 1, 2, 3, 34, 99}

st.remove( 99 )
print( st ) #   {65, 1, 2, 3, 34}


# ----------
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
# ---> {'orange', 'banana', 'pear', 'apple'}
'orange' in basket                 # fast membership testing
# ---> True
'crabgrass' in basket
# ---> False

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
# ---> {'a', 'r', 'b', 'c', 'd'}
a - b                              # letters in a but not in b
# ---> {'r', 'd', 'b'}
a | b                              # letters in a or b or both
# ---> {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                              # letters in both a and b
# ---> {'a', 'c'}
a ^ b                              # letters in a or b but not both
# ---> {'r', 'd', 'b', 'm', 'z', 'l'}


# ----------
a = {x for x in 'abracadabra' if x not in 'abc'}
# --> {'r', 'd'}


# ----------
for idx, val in enumerate( st ):
    print( idx, val )

# -->
# 0 65
# 1 1
# 2 2
# 3 3
# 4 34
# 5 99


# ----------
A = { 1, 2, 5, 6, 8, 9 }
B = { 1, 6, 8, 12, 14, 145}
print( A & B )  #   {8, 1, 6}   # A Intersection B
print( A | B )  #   {1, 2, 5, 6, 8, 9, 12, 14, 145}   # A Union B



# ----------
# ----------
# ----------

