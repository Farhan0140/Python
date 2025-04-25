
from _1_Person import Person
from _3_Shop import Shop
from _4_Item import Item
from _5_Customer import Customer


class Seller( Person ):
    def __init__(self, name, email, password):
        self.s_products = []
        super().__init__(name, email, password)

    
    def add_product(self, shop, item):
        tmp = item
        for product in self.s_products:
            if product.name.lower() == tmp.name.lower():
                product.quantity += tmp.quantity
                print(' *  Quantity Updated  * ')
                return
        self.s_products.append(tmp)
        shop.add_item(item)


    def remove_product(self, shop, item_name):
        shop.remove_item(item_name)
        for product in self.s_products:
            if product.name.lower() == item_name.lower():
                self.s_products.remove(product)
                break


    def see_products(self):
        print(f' * ______ Seller {self.name.capitalize()}\'s Products ______ *  ')
        print('Name\tPrice\tQuantity\tPer')
        for product in self.s_products:
            print(f'{product.name.capitalize()}\t{product.price}\t{product.quantity}\t\t{product.type}')
        print('_____________________________________') 
        print()
        

