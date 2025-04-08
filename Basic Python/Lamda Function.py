
def Power(a, b):
    return pow(a, b)
print( Power(2, 3) )  #   8



Power = lambda a, b: pow(a, b)
print( Power(2, 3) )    #   8
print( Power(2, 10) )    #   1024



# ------------>

Double = lambda x: x * 2

arr = [2, 5, 6, 8, 9, 2, 3, 4, 5]
new_arr = map(Double, arr)      # return object

print(new_arr)  #   <map object at 0x0000027D512FAFB0>

print( list(new_arr) )  #   [4, 10, 12, 16, 18, 4, 6, 8, 10]



# ------------>

arr = [2, 5, 6, 8, 9, 2, 3, 4, 5]
new_arr = map(lambda x: x * 2, arr)      # return object
print( list(new_arr) )  #   [4, 10, 12, 16, 18, 4, 6, 8, 10]




# ------------>

actors = [
    { 'Name': 'Farhan', 'Age': 23 },
    { 'Name': 'Safa', 'Age': 32 },
    { 'Name': 'Fahim', 'Age': 43 },
    { 'Name': 'Sadi', 'Age': 49 },
    { 'Name': 'Nafi', 'Age': 30 },
    { 'Name': 'Mahi', 'Age': 25 },
    { 'Name': 'Tamim', 'Age': 16 }
]

juniors = filter( lambda person: person['Age'] <= 30, actors )

print( list(juniors) )
# --->
# [
#     {'Name': 'Farhan', 'Age': 23}, 
#     {'Name': 'Nafi', 'Age': 30}, 
#     {'Name': 'Mahi', 'Age': 25}, 
#     {'Name': 'Tamim', 'Age': 16}
# ]

