class ShoppingCart(object):
    def __init__(self):
        self.total = 0
        self.items = dict()
        # Add an Item
        
    def add_item(self, item_name, quantity, price):
        if item_name and quantity and price:
            if type(item_name) == str and type(quantity) == int and type(price) == int:
                if item_name in self.items:
                    self.items[item_name] += quantity
                else:
                    self.items[item_name] = quantity
                self.total += quantity * price
                
                #Remove an Item 
    def remove_item(self, item_name, quantity, price):
        if item_name and quantity and price:
            if type(item_name) == str and type(quantity) == int and type(price) == int:
                if item_name in self.items:
                    if quantity > self.items[item_name]:
                        del self.items[item_name]
                    else: 
                        self.items[item_name] -= quantity
                    self.total -= quantity * price
                    
                #   Checkout
    def checkout(self, cash_paid):
        if cash_paid and type(cash_paid) == int:    
            if self.total > cash_paid:
                return "Cash paid not enough"
            else:
                return cash_paid - self.total
class Shop(ShoppingCart):
    def __init__(self):
        self.quantity = 100
    def remove_item(self):
        self.quantity -= 1