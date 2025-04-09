# ________Simple Class___________

class info:

    name = 'Farhan'
    age = 24
    dept = 'CSE'


obj = info()
print( obj.name )   #   Farhan
print( obj.dept )   #   CSE






# __________Methods_____________

# Error
class info:

    name = 'Farhan'
    age = 24
    dept = 'CSE'

    def call():
        print( 'Hi' )


obj = info()
print( obj.call() )   
"""
Traceback (most recent call last):
  File "e:\Practice\Temp.py", line 14, in <module>
    print( obj.call() )
           ~~~~~~~~^^
TypeError: info.call() takes 0 positional arguments but 1 was given
"""

# --->  Self Parameter


class info:

    name = 'Farhan'
    age = 24
    dept = 'CSE'

    def call(self):
        print( 'Hi' )


obj = info()
print( obj.call() )   # Hi


# EX:  _______________________


class info:
    
    def send_sms(self, phone, msg) :
        print( f'Sending sms to {phone} ans massage is: {msg}' )


obj = info()
print( obj.send_sms(+8801403, 'You Failed 2 subject.') )   # Sending sms to 8801403 ans massage is: You Failed 2 subject.






# _____________________ Constructors and ( __init__ ) ___________________


class Phone:
    manufactured = 'China'
    def __init__ (self, owner, brand, price):
        self.owner= owner
        self.brand = brand
        self.price = price


my_phone = Phone("Farhan", "Honor", 9999)
print( my_phone.owner, my_phone.brand, my_phone.price)  #   Farhan Honor 9999

my_2nd_phone = Phone("Farhan", "Oppo", 1200)
print( my_2nd_phone.owner, my_2nd_phone.brand, my_2nd_phone.price)  #   Farhan Oppo 1200





# ________ Class Attributes vs instance attributes ___________

#   Class Attributes
class Shop:
    lst = []

    def __init__(self, buyer):
        self.name = buyer
        
    def add_to_cart(self, product_name):
        self.lst.append( product_name )
        


farhan = Shop('Farhan')
farhan.add_to_cart('Ram 32 GB')
farhan.add_to_cart('Pendrive')
farhan.add_to_cart('Headphone')
print(farhan.name)
print(farhan.lst)
"""
Farhan
['Ram 32 GB', 'Pendrive', 'Headphone']
"""


safa = Shop('Safa')
safa.add_to_cart('Monitor')
print(safa.name)
print(safa.lst)
"""
Safa
['Ram 32 GB', 'Pendrive', 'Headphone', 'Monitor']
"""


nafi = Shop('Nafi')
nafi.add_to_cart('Gamepad')
nafi.add_to_cart('Keybord')
print(nafi.name)
print(nafi.lst)
"""
Nafi
['Ram 32 GB', 'Pendrive', 'Headphone', 'Monitor', 'Gamepad', 'Keybord']
"""


"""
কিন্তু আউটপুট এবং কোড ২ টা যদি আমরা খেয়াল করি তাহলে দেখব যে nafi add_to_cart() করার পরে যদিও আমরা nafi.lst. এইতাবে ত্যালুগুলোকে
প্রিন্ট করছি তারপরও সেখানে আগের অবজেক্ট এর এড করা প্রোডাক্ট্র ও রয়ে গেছে এই জিনিসটাই হচ্ছে ক্লাস এট্রিবিউট অর্থাৎ এই এট্রিবিউট টা এই ক্লাস এর প্রোপাটি
এই ক্লাস এর যেকোনো এট্রিবিউট দিয়ে যদি এই এট্রিবিউট এ কোনো চেঞ্জ হয় সেটা ডিরেক্টর এই এট্রিবিউট এই চেঞ্জ করবে
"""


#   Instance Attributes

class Shop:

    def __init__(self, buyer):
        self.name = buyer
        self.lst = []
        
    def add_to_cart(self, product_name):
        self.lst.append( product_name )


farhan = Shop('Farhan')
farhan.add_to_cart('Ram 32 GB')
farhan.add_to_cart('Pendrive')
farhan.add_to_cart('Headphone')
print(farhan.name)
print(farhan.lst)
"""
Farhan
['Ram 32 GB', 'Pendrive', 'Headphone']
"""


safa = Shop('Safa')
safa.add_to_cart('Monitor')
print(safa.name)
print(safa.lst)
"""
Safa
['Monitor']
"""


nafi = Shop('Nafi')
nafi.add_to_cart('Gamepad')
nafi.add_to_cart('Keybord')
print(nafi.name)
print(nafi.lst)
"""
Nafi
['Gamepad', 'Keybord']
"""

# এইবার দেখুন যখন যেই অবজেক্ট যেটা যেটা add_to_cart() এড করছে সেটা শুধু সেই অবজেক্ট এর আন্ডারেই এড হয়ছে



# --