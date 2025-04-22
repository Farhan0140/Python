
import _1_User as usr
import _5_Menu as mnu
import _8_Order as odr


class Customer( usr.User ):

    def __init__(self, name, phone, email, address):
        self.cart = odr.Order()
        super().__init__(name, phone, email, address)


    def show_menu(self, restaurant):
        restaurant.menu.show_menu()

    
    def add_to_cart(self, restaurant, item_name, quantity=1):
        item = restaurant.menu.find_item(item_name)

        if item:
            if item.quantity >= quantity:
                new_quantity = item.quantity - quantity
                item.quantity = quantity
                self.cart.add_item(item)
                print(f' * { item_name } is added successfully the Cart * ')
                restaurant.menu.update_item(item_name, new_quantity)
            else:
                print(f' * There are not that many products. {item.quantity} products are available * ')
        else:
            print(f' * {item_name} Not Found * ')


    def remove_from_cart(self, restaurant, item_name):
        item_menu = restaurant.menu.find_item(item_name)
        item_cart = self.cart.find_item(item_name)

        if item_cart:
            qnt = 0
            for itm, quantity in self.cart.items.items():
                if itm.item_name.lower() == item_name.lower():
                    qnt = quantity
                    break
            
            if item_menu:
                restaurant.menu.update_item_1(item_name, qnt)
            else:
                restaurant.menu.add_item(item_cart)

            print(f' * {item_name} removed successfully * ')
            self.cart.remove_item(item_cart)
        else:
            print(f' * {item_name} Not Found * ')


    def view_cart(self):
        print('  * ____ Cart ____ * ')
        print('Name\tPrice\tQuantity')
        for itm, quantity in self.cart.items.items():
            print(f'{itm.item_name}\t{itm.price}\t{quantity}')

        print(f'Total Price: {self.cart.total_price()}')


