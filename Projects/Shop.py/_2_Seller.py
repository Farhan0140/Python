
from _1_Person import Person
from _3_Shop import Shop
from _4_Item import Item


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
        



# _sop = Shop('Shopno', 'asd')

# _1_itm = Item('Page', 5, 1000, 'pcs')
# _2_itm = Item('Pen', 5, 500, 'pcs')


# _s1 = Seller('Baten', 'baten@gmail.com', '69963')

# _s1.add_product(_sop, _1_itm)
# _s1.add_product(_sop, _2_itm)
# _s1.add_product(_sop, _2_itm)

# _s1.see_products()


# _3_itm = Item('Egg', 15, 150, 'pcs')
# _4_itm = Item('Rice', 180, 10, 'kg')
# _5_itm = Item('Rice', 180, 10, 'kg')
# _6_itm = Item('Rice', 180, 10, 'kg')
# _7_itm = Item('Rice', 180, 10, 'kg')

# _s2 = Seller('Akash', 'akash@gmail.com', '1234')


# _s2.add_product(_sop, _3_itm)
# _s2.add_product(_sop, _4_itm)
# _s2.add_product(_sop, _5_itm)
# _s2.add_product(_sop, _6_itm)
# _s2.add_product(_sop, _7_itm)

# _s2.remove_product(_sop, 'rice')
# _s2.see_products()





