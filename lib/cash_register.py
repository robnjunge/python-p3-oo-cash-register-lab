
#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0, items=[], last_item=0):
        self.discount = discount
        self.total = total
        self.items = []
        self.last_item = last_item

    def add_item(self, title, price, quantity=1):
        self.total += price*quantity
        n = quantity
        while n > 0:
            self.items.append(title)
            n -= 1
            
        self.last_item = price*quantity

    def apply_discount(self):
        if self.discount != 0:
            self.total -= (self.discount / 100.0) * self.total
            print(f"After the discount, the total comes to ${self.total:g}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_item
        self.items = self.items[:-1]