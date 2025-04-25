

class Order:
    def __init__(self):
        self.cart = {}
        self.TotalPrice = 0


    def find_product(self, product_name):
        for product in self.cart:
            if product.name.lower() == product_name.lower():
                return product
            
        return None
    

    def add_product(self, item):

        if item in self.cart:
            self.TotalPrice -= item.price * self.cart[item]
            self.cart[item] += item.quantity
            self.TotalPrice += item.price * self.cart[item]
            print(' *  Quantity Updated  * ')

        else:
            self.cart[item] = item.quantity
            self.TotalPrice += item.price * item.quantity
            print(' *  Item successfully added to cart  * ')


    def remove_product(self, item):
        self.TotalPrice -= (self.cart[item] * item.price)
        print(' * Item Removed Successfully * ')
        del self.cart[item]


    def clear_cart(self):
        self.TotalPrice = 0
        self.cart = {}


    def total_price(self):
        print(f'--> Total Price: {self.TotalPrice}')


    


