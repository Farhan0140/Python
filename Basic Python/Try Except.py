
# res = 25 / 0

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
"""



try:
    res = 25 / 0
except:
    print( "Error Occurred" )   #   Error Occurred
print( "Done" ) #   Done



# -----------------------

try:
    res = 25 / 0
except:
    print( "Error Occurred" )   #   Error Occurred
finally:
    print( "Finally Here" )     #   Finally Here
print( "Done" ) #   Done


# -->


try:
    res = 25 / 5
except:
    print( "Error Occurred" )
finally:
    print( "Finally Here" )     #   Finally Here
print( "Done" ) #   Done



# -----------------------

