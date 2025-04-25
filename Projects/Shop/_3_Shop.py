


class Shop:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.products = []


    def find_item(self, item_name):
        for product in self.products:
            if item_name.lower() == product.name.lower():
                return product
            
        return None


    def add_item(self, item):
        product = self.find_item(item.name)

        if product:
            product.quantity += item.quantity

        else:
            self.products.append(item)
            print(' *  Item successfully added  * ')


    def remove_item(self, item_name):
        item = self.find_item(item_name)
        self.products.remove(item)
        print(f' *  {item_name} Successfully Removed  * ')


    def update_item(self, item_name, quantity):
        product = self.find_item(item_name)
        if quantity == 0:
            self.products.remove(product)
            return
        
        product.quantity = quantity


    def show_all_products(self):
        print(f'\t* _____ Shop _____ * ')
        print('Name\tPrice\tQuantity\tPer')
        for product in self.products:
            print(f'{product.name.capitalize()}\t{product.price}\t{product.quantity}\t\t{product.type}')
        print('_____________________________________')    



