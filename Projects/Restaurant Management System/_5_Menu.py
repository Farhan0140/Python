

class Menu:
    def __init__(self):
        self.items = []

    def find_item(self, item_name):
        for item in self.items:
            if item.item_name.lower() == item_name.lower():
                return item
            
        return None
    

    def add_item(self, item):
        self.items.append(item)
        print(f' * { item.item_name } is added successfully the list * ')


    def update_item(self, item_name, quantity):
        for item in self.items:
            if item.item_name.lower() == item_name.lower():
                if quantity > 0:
                    item.quantity = quantity
                    return
                else:
                    self.items.remove(item)
                    return
                
    def update_item_1(self, item_name, quantity):
        for item in self.items:
            if item.item_name.lower() == item_name.lower():
                    item.quantity += quantity


    def remove_item(self, item_name):
        item = self.find_item(item_name)

        if item:
            self.items.remove(item)
            print(f' * { item_name } is removed successfully from the list * ')
            
        else:
            print(f' * {item_name} Not Found * ')


    def show_menu(self):
        print('  * ____ Menu ____ * ')
        print('Name\tPrice\tQuantity')

        for item in self.items:
            print(f'{item.item_name}\t{item.price}\t{item.quantity}')



