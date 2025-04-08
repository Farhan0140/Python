
s = 'Farhan'
s1 = "Nadim"
s2 = """
     
     Farhan
     Nadim
     Sourav

     """

s3 = 'Farhan\'s'  # Escape


# ----------------------------
print('py' in 'python')   #  True


# ----------------------------
print( "The sum of 100 + 12 is {0}".format(100 + 12) )  #   The sum of 100 + 12 is 112


# ----------------------------
s = "farhan"
s = s.upper()
print( s )  #   FARHAN


# ----------------------------
s = "fARHan"
s = s.lower()
print( s )  #   farhan


# ----------------------------
s = "fARHan"
print( s.isupper() )    #   False


# ----------------------------
s = "farhan"
print( s.islower() )    #   True


# ----------------------------
s = '7'
print( s.isdigit() )    #   True


# ----------------------------
s = 'A'
print( s.isalpha() )    #   True


# ----------------------------

s = 'Rahim'

s[0] = 'F'
print(s)
"""
Traceback (most recent call last):
  File "e:\Practice\Temp.py", line 2, in <module>
    s[0] = 'F'
    ~^^^
TypeError: 'str' object does not support item assignment

"""


s = list(s)
print(s)    #   ['R', 'a', 'h', 'i', 'm']

s[0] = 'F'
print(s)    #   ['F', 'a', 'h', 'i', 'm']

s = "".join(s)
print(s)    #   Fahim




# ----------------------------
# ----------------------------
# ----------------------------
# ----------------------------
# ----------------------------