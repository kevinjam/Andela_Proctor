class ShoppingCart(object):
    def __init__(self):
        self.total = 0
        self.items = {}
        # Add an Item


    def add_item(self, item_name, quantity, price):
        item_cost = quantity * price
        self.total += item_cost
        self.items[item_name] = quantity
                # Remove an Item

    def remove_item(self, item_name, quantity, price):
        if self.items[item_name] > quantity:
            self.items[item_name] = self.items[item_name] - quantity
            self.total -= quantity * price
        else:
            self.total -= price * self.items[item_name]
            del self.items[item_name]
                    #   Checkout

    def checkout(self, cash_paid):
            if  cash_paid>= self.total:
                balance = cash_paid - self.total
                return balance
            else:
                return "Cash paid not enough"

class Shop(ShoppingCart):
    def __init__(self):
        self.quantity = 100
    def remove_item(self):
        self.quantity -= 1
