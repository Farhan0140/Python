from math import *

x = ceil(3.0001)
print(x)    #   4

x = floor(3.9999)
print(x)    #   3


x = round(3.49)
print(x)    #   3   < .50

x = round(3.51)
print(x)    #   4   >= .50



# ----------------------
from random import *



# 0.0 <= x <= 1.0
print( random() )   #   0.264837265179771
print( random() )   #   0.10452259858690793
print( random() )   #   0.1309439344782226


print( choice( ['Farhan', 'Safa', 'Tamim', 'Nafi'] ) )   #   Safa




# ----------------------
from time import *



print("Hi, --> ")
#     Sec
sleep(2)
print( "Baten" )