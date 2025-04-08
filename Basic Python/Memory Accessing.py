
x = 10
y = 10

print( id(x) )  #   140721429546184
print( id(y) )  #   140721429546184
#                   Python stores the same value in one memory location 


p = 10
q = 11

print( id(p) )  #   140721429546184     # Same as x and y
print( id(q) )  #   140721429546216


# --