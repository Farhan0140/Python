numbers = [12, 56 , 98, 78, 56, 12, 26, 98]
#           Name         Home      Age  Profession
person1 = ['Kala Chan', 'kalipur', 23, 'student']
person2 = ['Kala ', 'kalipur', 25, 'Teacher']

# key value pair
# dicionary
# object
# hash table !
# Overlap with Set
# { Key:Value, Key : Value, ...... }


# --------------
person = {
    'Name' : 'Farhan',
    'Address' : 'Dhaka',
    'Age' : 26,
    'Profession' : 'Student'
}

print( person ) #   {'Name': 'Farhan', 'Address': 'Dhaka', 'Age': 26, 'Profession': 'Student'}
print( person['Name'] ) #   Farhan
print( person['Profession'] )   #   Student

print( person.keys() )  #   dict_keys(['Name', 'Address', 'Age', 'Profession'])
print( person.values() )    #   dict_values(['Farhan', 'Dhaka', 26, 'Student'])



# --------------
person['Language'] = 'Bangla'
print( person ) #   {'Name': 'Farhan', 'Address': 'Dhaka', 'Age': 26, 'Profession': 'Student', 'Language': 'Bangla'}


person['Name'] = 'Nadim'
print( person ) #   {'Name': 'Nadim', 'Address': 'Dhaka', 'Age': 26, 'Profession': 'Student'}



# --------------
del person['Profession']
print( person ) #   {'Name': 'Farhan', 'Address': 'Dhaka', 'Age': 26}


# --------------
for key, val in person.items():
    print( key, ":", val )

# -->
# Name : Farhan
# Address : Dhaka
# Age : 26
# Profession : Student



# --------------
