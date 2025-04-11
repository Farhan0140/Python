import os

def clr_scr():
    os.system('cls' if os.name == 'nt' else 'clear')


class Bank:

    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.total_amount = 0
        self.min_amount = 500
        self.max_amount = 10000

    def check_bal(self):
        return self.total_amount

    def deposit(self, amount):
        if amount > 0:
            print(f'Old balance {self.total_amount} taka only')
            self.total_amount += amount
            print(f'New balance {self.total_amount} taka only')
        else:
            print( f'Invalid amount' )
        
    def withdraw(self, amount):
        if amount > self.max_amount:
            print(f'You can\'t Withdraw more than {self.max_amount} taka')
        elif amount < self.min_amount:
            print(f'You need to Withdraw more than {self.min_amount} taka')
        elif amount < 0:
            print( f'Invalid amount' )
        elif self.total_amount == 0:
            print(f'You can\'t withdraw because your corrent balance {self.total_amount} \n please deposit')
        else:
            if self.total_amount - amount < 0:
                print(f'Insufficient Balance. Current Balance is {self.total_amount}')
            else:
                self.total_amount -= amount
                print(f'Current Balance is: {self.total_amount} taka only')


name = input('Enter Your name to create account\n--> ')
age = int(input('Enter your age\n--> '))
obj = Bank(name, age)

while(True):
    clr_scr()
    print(f'{1}. Check Balance\n{2}. Deposit\n{3}. Withdraw\n{4}. Exit')
    chk = int(input('--> '))

    if chk == 1:
        clr_scr()
        print(f'{obj.check_bal()} taka only')

        back = input('B. Back\n--> ')
        if back == 'b' or back == 'B':
            continue
    elif chk == 2:
        clr_scr()
        amount = int(input('Enter total amount to Deposit: '))
        obj.deposit(amount)

        back = input('B. Back\n--> ')
        if back == 'b' or back == 'B':
            continue
    elif chk == 3:
        clr_scr()
        amount = int(input('Enter total amount to Withdraw: '))
        obj.withdraw(amount)

        back = input('B. Back\n--> ')
        if back == 'b' or back == 'B':
            continue
    else:
        break


