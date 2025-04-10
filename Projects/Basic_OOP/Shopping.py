import os
def clr_scr():
    os.system('cls' if os.name == 'nt' else 'clear')



class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
        self.total_taka = 0

    def add_to_cart(self, item, price, quantity):
        product = {'Item:': item, 'Price': price, 'Quantity': quantity}
        self.cart.append(product)
        self.total_taka += (price * quantity)
        print(f'Added to cart successfully')

    def remove_item(self, item_n):
        chk = input('Are you sure? [Y/N]\n--> ')

        if chk.lower() == 'y':

            for i, items in enumerate( self.cart ):
                if items['Item:'] == item_n:
                    self.total_taka -= (items['Price'] * items['Quantity'])
                    del self.cart[i]
                    print(f'Removed "{item_n}" from the cart.')
                    return
        else:
            return

        print(f'{item_n} Not Found')

    
    def checkout(self, amount):
        total = 0
        for items in self.cart:
            total += ( items['Price'] * items['Quantity'] )
        
        if total > amount:
            print(f'Please provide {total - amount} more')
        elif total == amount:
            print('Payment successful, Here are your products')
            self.cart.clear()
            self.total_taka = 0
        else:
            print(f'Here are your products and extra {amount - total} taka')
            self.cart.clear()
            self.total_taka = 0




name = input('Enter your name to create the bill\n--> ')
obj = Shopping(name)

while(True):
    clr_scr()
    print(f'{1}. Add to Cart\n{2}. Remove Items\n{3}. Checkout\n{4}. Exit')
    chk = int(input('--> '))

    if chk == 1:
        clr_scr()
        p_name = input('Enter Product name: ')
        p_price = int(input('Enter product price: '))
        p_q = int(input('Enter product quantity: '))

        obj.add_to_cart(p_name, p_price, p_q)

        back = input('B. Back\n--> ')
        if back.lower() == 'b':
            continue

    elif chk == 2:
        clr_scr()
        r_item = input('Enter product name to remove from cart: ')
        obj.remove_item(r_item)

        back = input('B. Back\n--> ')
        if back.lower() == 'b':
            continue

    elif chk == 3:
        clr_scr()
        print(f'Your bill is {obj.total_taka} taka only')
        amount = int(input('Enter the amount to confirm the order: '))
        obj.checkout(amount)

        back = input('B. Back\n--> ')
        if back.lower() == 'b':
            continue

    else:
        break





# ------------------------