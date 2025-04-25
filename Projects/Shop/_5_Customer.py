
from _1_Person import Person
from _6_Order import Order


class Customer( Person ):
    def __init__(self, name, email, password):
        self.cart = Order()
        super().__init__(name, email, password)


    def all_products(self, shop):
        shop.show_all_products()


    def add_to_cart(self, shop, item_name, quantity=1):
        product = shop.find_item(item_name)

        if quantity <= product.quantity:
            new_quantity = product.quantity - quantity
            product.quantity = quantity
            self.cart.add_product(product)
            shop.update_item(item_name, new_quantity)

        else:
            print(f' *  The available product quantity is {product.quantity}  * ')


    def remove_from_cart(self, shop, item_name):
        product = shop.find_item(item_name)
        item = None
        
        for key, value in self.cart.cart.items():
            if key.name.lower() == item_name.lower():
                product.quantity += value
                item = key
                break

        self.cart.remove_product(item)


    def make_payment(self):
        print(f'Do you want to pay {self.cart.TotalPrice} BDT')
        s = input('Type \'Confirm\' to pay bill: ')
        if s.lower() == 'confirm':
            self.cart.clear_cart()



    def view_cart(self):
        print(f'\t* _____ Cart _____ * ')
        print('Name\tPrice\tQuantity\tTotal Price')
        for product, quantity in self.cart.cart.items():
            print(f'{product.name.capitalize()}\t{product.price}\t{quantity}\t\t{(product.price * quantity)}')
        self.cart.total_price()
        print('_____________________________')

